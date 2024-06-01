import json
import logging
import custom_tools

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openai import OpenAI
from config import *

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

slack_app = App(token=SLACK_BOT_TOKEN)

# This is a simple in-memory lookup to associate slack threads with OpenAI threads
# TODO: Save this to a database instead of using an in-memory lookup
thread_id_lookup = {}

# Get the bot user ID
auth_response = slack_app.client.auth_test()
bot_user_id = auth_response["user_id"]
logger.info(f"{BOT_NAME} User ID = {bot_user_id}")

openai_client = OpenAI()
assistant = openai_client.beta.assistants.retrieve(OPENAI_ASSISTANT_ID)


def invoke_llm(e, text):
    # See if there is an existing thread that can be used
    thread = None
    thread_key = "im" if e["channel_type"] == "im" else e.get("thread_ts", e["ts"])
    thread_id = thread_id_lookup.get(thread_key)
    if thread_id is not None:
        thread = openai_client.beta.threads.retrieve(thread_id)

    # If no existing thread was found, create a new one
    if thread is None:
        thread = openai_client.beta.threads.create(
            metadata={
                "channel": e.get("channel", ""),
                "channel_type": e.get("channel_type", ""),
                "ts": e.get("ts", ""),
                "thread_ts": e.get("thread_ts", ""),
            }
        )
        logger.info(f"Created new OpenAI thread: {thread.id}")
        thread_id_lookup[thread_key] = thread.id
    else:
        logger.info(f"Using existing OpenAI thread: {thread.id}")
    logger.debug(thread)

    # TODO: Set a token or message limit for the thread, to avoid excessive token usage
    # TODO: Include the user's name in the message (update the assistant prompt to show how to interpret this)

    # Add a message to the thread
    message_content = text.replace(f"<@{bot_user_id}>", BOT_NAME)
    message = openai_client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message_content
    )
    logger.info(f"Added message to thread: {message_content}")
    logger.debug(message)

    # Run the assistant
    run = openai_client.beta.threads.runs.create_and_poll(assistant_id=assistant.id, thread_id=thread.id)
    logger.info(f"Assistant run completed with status {run.status}")
    logger.debug(run)

    try:
        # Call any required tools
        while run.status == 'requires_action':
            logger.info("Run requires one or more actions")
            tool_outputs = []
            for tool in run.required_action.submit_tool_outputs.tool_calls:
                logger.info(f"Calling tool function {tool.function.name} with arguments {tool.function.arguments}")
                custom_tool_function = getattr(custom_tools, tool.function.name)
                tool_output = json.dumps(custom_tool_function(**json.loads(tool.function.arguments)))
                logger.info(f"tool output = {tool_output}")
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": tool_output
                })
            if tool_outputs:
                run = openai_client.beta.threads.runs.submit_tool_outputs_and_poll(thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs)
                logger.info(f"Assistant run completed with status {run.status}")
                logger.debug(run)
            else:
                raise Exception("No tool outputs were generated")

        # Check run status to make sure it is completed
        if run.status != 'completed':
            raise Exception(f"Run status was {run.status}")

        # Return the assistant's responses
        messages = openai_client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id)
        logger.debug(messages)
        responses = []
        for message in messages.data:
            if message.role == "assistant":
                for c in message.content:
                    if c.type == "text":
                        logger.info(f"Assistant response: {c.text.value}")
                        responses.append(c.text.value)
                    else:
                        logger.warning(f"Unsupported message content type: {c.type}")
                        responses.append(f"Unsupported message content type: {c.type}")
        return responses
    except Exception:
        try:
            openai_client.beta.threads.runs.cancel(thread_id=thread.id, run_id=run.id)
        except Exception as e:
            logger.error(f"Error cancelling run: {e}")
        raise


@slack_app.event("message")
def handle_message_events(body, client, say):
    slack_thread_ts = None
    try:
        logger.info("Slack message received")
        logger.debug(json.dumps(body, indent=2))

        e = body["event"]
        text = e["text"].strip()
        slack_thread_ts = e.get("thread_ts", e["ts"])

        # Handle direct messages
        if e["channel_type"] == "im":
            logger.info("Responding to slack direct message")
            responses = invoke_llm(e, text)
            for response in responses:
                say(response)
            return

        # Handle mentions in channels
        if e["channel_type"] == "channel" and e["text"].startswith(f"<@{bot_user_id}>"):
            logger.info("Responding to mention in slack channel")
            responses = invoke_llm(e, text)
            for response in responses:
                say(response, thread_ts=slack_thread_ts)
            return

        logger.info("No action taken for this slack message")
    except Exception as e:
        try:
            logger.error(e)
        except Exception as e:
            print(e)
        try:
            if slack_thread_ts is None:
                say(f":boom: An error occurred: {e}")
            else:
                say(f":boom: An error occurred: {e}", thread_ts=slack_thread_ts)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    slack_handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    slack_handler.start()
