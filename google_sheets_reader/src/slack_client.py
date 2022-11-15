from slack_sdk import WebClient
from google_sheets_reader.environment_variables import environment_variables
from datetime import datetime


def _get_today() -> str:
    return datetime.today().strftime("%Y/%m/%d")


# Send update message in clack channel
def send_message(message: str) -> None:
    client = WebClient(environment_variables.BOT_TOKEN)
    res = client.chat_postMessage(channel=environment_variables.CHANNEL_ID, text=message)

    print(f"{res}")


def send_reminder_message() -> None:
    client = WebClient(environment_variables.BOT_TOKEN)
    res = client.chat_postMessage(channel=environment_variables.CHANNEL_ID, text=f"Remember to update the date and status of tickets you worked on today by 9pm.\nDate today: {_get_today()}")

    print(f"{res}")