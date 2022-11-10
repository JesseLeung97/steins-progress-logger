from dotenv import find_dotenv, load_dotenv
from os import getenv


# Loads and contains variables set in .env
class Env:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.CHANNEL_ID = getenv("CHANNEL_ID")
        self.SPREADSHEET_ID = getenv("SPREADSHEET_ID")
        self.GOOGLE_API_CREDENTIALS = getenv("GOOGLE_API_CREDENTIALS")


# Global instance of env variables
environment_variables = Env()
