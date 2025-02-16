import json
import functions_framework
from app.helpers import notification_helper
from utils import logger

@functions_framework.http
def handle_alerts(req):
    try:
        if req.method != "POST":
            return json.dumps({"error": "Method not allowed"}), 405, {"ContentType": "application/json"}

        # Retrieving data from the request
        jsonData = req.get_json()
        if not jsonData or "slack_block" not in jsonData:
            return json.dumps({"error": "Missing or invalid slack_block"}), 400, {"ContentType": "application/json"}

        slack_block = jsonData["slack_block"]
        success = notification_helper.notify(slack_block)

        if not success:
            return json.dumps({"error": "Failed to send Slack alert"}), 500, {"ContentType": "application/json"}

    except Exception as e:
        error_message = "Error while handling request for slack alert service"
        logger.error(f"{error_message}: {e}", exc_info=True)
        return json.dumps({"message": error_message}), 500, {"ContentType": "application/json"}

    return json.dumps({"Success": True}), 200, {"ContentType": "application/json"}
