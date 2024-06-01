import custom_tools

from openai import OpenAI
from config import *

openai_client = OpenAI()

assistant_args = {
    "name": f"{BOT_NAME}Assistant",
    "description": f"{BOT_NAME} Assistant",
    "instructions": f"""
        You are a helpful assistant named {BOT_NAME}.
        You can use the provided tools to help you answer questions.
        It is important that your answers are accurate and helpful.
        If you don't know the answer to a question, you should say so.
        If you need more information to answer a question, you should ask for it.
        You must never provide false or misleading information.
        If you are sending an email or sending any other form of communication on behalf of a user, you should identify yourself as {BOT_NAME}.
                """.strip(),
    "model": "gpt-3.5-turbo",
    # "model": "gpt-4o",
    "tools": custom_tools.tools
}

if OPENAI_ASSISTANT_ID is not None:
    assistant = openai_client.beta.assistants.update(OPENAI_ASSISTANT_ID, **assistant_args)
    print(f"Updated OpenAI Assistant ID: {assistant.id}")
else:
    assistant = openai_client.beta.assistants.create(**assistant_args)
    print(f"Created OpenAI Assistant ID: {assistant.id}")
