import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

if ENVIRONMENT == "development":
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()

TESTING = os.environ.get("TESTING")
DEBUG = os.environ.get("DEBUG")
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")
