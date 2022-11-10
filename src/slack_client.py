from slack_sdk import WebClient
from environment_variables import environment_variables

# Send update message in clack channel
def send_message(message: str) -> None:
    client = WebClient(environment_variables.BOT_TOKEN)
    #res = client.chat_postMessage(channel=environment_variables.CHANNEL_ID, text=message)

    print(f"{message}")