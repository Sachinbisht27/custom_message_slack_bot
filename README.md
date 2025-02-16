# Slack Alert Service

A lightweight and scalable Slack Alert Service built with Python and Google Cloud Functions. This service listens for incoming HTTP POST requests containing Slack messages and sends notifications to a specified Slack channel.

## Features
- Cloud Function-based alert system
- Secure Slack API integration
- Simple HTTP POST-based message handling
- Error logging and exception handling

## Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.8+
- Google Cloud SDK (`gcloud` CLI)
- Virtual environment (`venv` or `virtualenv`)
- A Slack Bot Token with `chat:write` permissions

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Sachinbisht27/custom_message_slack_bot.git
cd slack-alert-service
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Set up your .env file by copying .env.example
```sh
cp .env.example .env
```
Add the following:
```sh
SLACK_TOKEN=your_slack_bot_token
SLACK_CHANNEL=your_channel_id
```

### 5. Deploy to Google Cloud Functions
Ensure you are authenticated with `gcloud` and have a project set up.
```sh
gcloud auth login
gcloud functions deploy handle_alerts \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated
```

### 6. Start the server by following command:
```sh
functions_framework --target=handle_alerts --debug
```

## Usage
To send an alert, make a `POST` request to your deployed function:

```sh
curl -X POST <YOUR_CLOUD_FUNCTION_URL> \
  -H "Content-Type: application/json" \
  -d '{"slack_block": {"blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "Hello, this is a test alert!"}}]}}'
```

## Logging
Logs can be monitored using Google Cloud Logging:
```sh
gcloud functions logs read handle_alerts
```

## License
This project is licensed under the MIT License.
