from google_sheets_reader.src.fetcher import get_data
from google_sheets_reader.src.assembler import DataCollector
from google_sheets_reader.src.slack_client import send_message


def update_progress():
    data = get_data()

    data_collector = DataCollector()
    data_collector.add_data(data)

    all_data = data_collector.to_string()

    send_message(message=all_data)
