import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from coinbot import CoinBot

app = Flask(__name__)

slack_event_adapter =  SlackEventAdapter("4844b24394d716658fb1f3390c150323", "/slack/events", app)

# Slack events token
slack_web_client = WebClient("PUT THE KEY/TOKEN HERE")

def flip_coin(channel):
    coin_bot = CoinBot(channel)

    message = coin_bot.get_message_payload();

    slack_web_client.chat_postMessage(**message)


@slack_event_adapter.on("message")
def message(payload):
    event = payload.get("event", {})

    text = event.get("text")
    print(text)

    if "flip coin" in text.lower():
        channel_id = event.get("channel")

        return flip_coin(channel_id)


if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)
