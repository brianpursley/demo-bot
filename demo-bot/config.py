import os
import dotenv

dotenv.load_dotenv()

BOT_NAME = os.getenv("BOT_NAME", "DemoBot")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

OPENAI_ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")
if not OPENAI_ASSISTANT_ID:
    raise ValueError("OPENAI_ASSISTANT_ID is not set")

SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
if not SLACK_APP_TOKEN:
    raise ValueError("SLACK_APP_TOKEN is not set")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
if not SLACK_BOT_TOKEN:
    raise ValueError("SLACK_BOT_TOKEN is not set")
