from typing import List
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from constants import Constants
from environment_variables import environment_variables

# Get Google Sheets API credentials from keys file
def _get_credentials() -> Credentials:
    return service_account.Credentials.from_service_account_file(
        Constants.SERVICE_ACCOUNT_FILE, scopes=Constants.SCOPES)


# Fetch data from Google Sheets using loaded credentials
def get_data() -> List[any]:
    creds = _get_credentials()

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=environment_variables.SPREADSHEET_ID,
        range=f"{Constants.SPREADSHEET_NAME}!{Constants.SPREADSHEET_RANGE}"
        ).execute()
    values = result["values"]
    
    return values
