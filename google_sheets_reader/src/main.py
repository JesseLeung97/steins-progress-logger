from google_sheets_reader.src.fetcher import get_dialog_data, get_server_data
from google_sheets_reader.src.assembler import DataCollector
from google_sheets_reader.src.slack_client import send_message, send_reminder_message


def update_progress():
    dialog_data = get_dialog_data()
    server_data = get_server_data()

    data_collector = DataCollector()
    
    data_collector.add_dialog_data(dialog_data)
    data_collector.add_server_data(server_data)

    all_data = data_collector.to_string()

    send_message(message=all_data)


def send_reminder():
    send_reminder_message()