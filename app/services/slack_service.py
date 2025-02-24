from ssl import SSLContext
import slack
import config
import traceback
from utils import logger

class SlackService:
    def __init__(self):
        self.token = config.SLACK_TOKEN
        self.sslcert = SSLContext()
        self.channel_name = config.SLACK_CHANNEL
        self.slack_client = slack.WebClient(
            token=self.token,
            ssl=self.sslcert,
        )

    def send_alert(self, slack_block):
        try:
            response = self.slack_client.chat_postMessage(
                channel=self.channel_name,
                blocks=slack_block.get("blocks", []),
            )
            logger.info(f"Alert Sent: {response}")
            return True
        except Exception as e:
            logger.error(f"Slack API Exception: {e}\n{traceback.format_exc()}")
            return False
