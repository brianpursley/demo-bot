import dotenv
import logging
import os

import custom_tools
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories.postgres import PostgresChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# TODO: Implement other tools (RAG)
# TODO: Auto-Summarize Chat History
# TODO: Save participating threads in a database
# TODO: Get bot name from Slack API on startup

dotenv.load_dotenv()
CHAT_HISTORY_DATABASE_URL = os.getenv("CHAT_HISTORY_DATABASE_URL")
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

participating_threads = set()

app = App(token=SLACK_BOT_TOKEN)

# Get the bot user ID
auth_response = app.client.auth_test()
bot_user_id = auth_response["user_id"]
bot_name = "DemoBot"
logger.info(f"{bot_name} User ID: {bot_user_id}")

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
# llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0)


tools = [
    *custom_tools.northwind_api_tools,
    *custom_tools.email_api_tools,
]

# prompt = hub.pull("hwchase17/openai-tools-agent")
# prompt = hub.pull("hwchase17/react-chat")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"""
You are a helpful assistant named {bot_name}.
It is important that your answers are accurate and helpful.
If you don't know the answer to a question, you should say so.
If you need more information to answer a question, you should ask for it.
You must never provide false or misleading information.
        """.strip()),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
logger.info(prompt)

agent = create_openai_tools_agent(llm, tools, prompt)


def llm_invoke(session_id, user_message) -> str:
    logger.debug(f"llm_invoke {session_id}: {user_message}")

    history = PostgresChatMessageHistory(connection_string=CHAT_HISTORY_DATABASE_URL, session_id=session_id)
    memory = ConversationBufferMemory(memory_key="chat_history", input_key="input", chat_memory=history, return_messages=True)
    # memory = ConversationBufferWindowMemory(memory_key="chat_history", input_key="input", chat_memory=history, return_messages=True)

    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

    response = agent_executor.invoke({"input": user_message})

    logger.debug(response)
    return response["output"]


def handle_exception(thread_ts, say, e):
    logger.error(e)
    if thread_ts is not None:
        say(thread_ts, f":boom: An error occurred: {e}")
    else:
        say(f":boom: An error occurred: {e}")


@app.event("message")
def handle_message_events(body, client, say):
    thread_ts = None
    try:
        logger.info("message")
        # logger.debug(json.dumps(body, indent=2))

        e = body["event"]
        thread_ts = e.get("thread_ts", e["ts"])
        text = e["text"].strip()
        llm_session_id = e["channel"] if e["channel_type"] == "im" else thread_ts

        # Always respond to a direct message in the direct message "channel"
        if e["channel_type"] == "im":
            say(llm_invoke(llm_session_id, text.replace(f"<@{bot_user_id}>", bot_name)))
            return

        # If the bot was mentioned, then start participating in the thread
        if thread_ts not in participating_threads:
            if e["text"].startswith(f"<@{bot_user_id}>"):
                participating_threads.add(thread_ts)

        # Respond in a thread if the bot is participating in that thread
        if thread_ts in participating_threads:
            # If the message starts with the mention of another user, then stop participating in this thread
            if e["text"].startswith(f"<@") and not e["text"].startswith(f"<@{bot_user_id}>"):
                participating_threads.remove(thread_ts)
                return

            # If the message is "<@bot_user_id> stop", then stop participating in this thread
            if e["text"].strip() == f"<@{bot_user_id}> stop":
                say("Okay, I will stop participating in this thread. You can @ mention if you want me to participate again.", thread_ts=thread_ts)
                participating_threads.remove(thread_ts)
                return

            say(llm_invoke(llm_session_id, text.replace(f"<@{bot_user_id}>", bot_name)), thread_ts=thread_ts)
    except Exception as e:
        handle_exception(thread_ts, say, e)


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
