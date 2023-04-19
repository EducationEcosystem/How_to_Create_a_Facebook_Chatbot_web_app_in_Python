from slack import WebClient
from coinbot import CoinBot

TOKEN = "xoxb-2696512543281-2683922310898-uMHN529oLXgZHHJ12F8yJ4yd";

# Create slack client
slack_web_client = WebClient(token=TOKEN)

# Get a new CoinBot
coin_bot = CoinBot("#general")

message = coin_bot.get_message_payload()

slack_web_client.chat_postMessage(**message)
