from google_sheets_reader.src.team_members import TeamMembers
from google_sheets_reader.src.progress_data import ProgressData
from google_sheets_reader.constants import Constants
from google_sheets_reader.src.progress_data import Status
from datetime import datetime


# Only add tasks which have been updated today
def _check_date(listed_date: str) -> bool:
    today = _get_today()
    if not listed_date.__eq__(today):
        return False
    return True


def _get_today() -> str:
    return datetime.today().strftime("%Y/%m/%d")

# return false if given member is not a team member
def _check_member(member: str) -> bool:
    if member.__eq__(TeamMembers.Simon) or member.__eq__(TeamMembers.Andreas) or member.__eq__(TeamMembers.Tom) or member.__eq__(TeamMembers.Jesse):
        return True
    return False


def _check_finished(status: str) -> bool:
    return status.__eq__(Status.Finished)


def _check_not_started(status: str) -> bool:
    return status.__eq__(Status.NotStarted)


# Gather progress data for each team member then convert to a message string
class DataCollector: 
    def __init__(self) -> None:
        self.all_data = {
            TeamMembers.Simon: ProgressData(),
            TeamMembers.Andreas: ProgressData(),
            TeamMembers.Tom: ProgressData(),
            TeamMembers.Jesse: ProgressData()
        }


    # Add  dialog data that is in progress, waiting for PR, or finished that day
    def _add_dialog_data(self, row) -> None:
        team_member_col = 1
        status_col = 2
        date_col = 3

        if ((not _check_member(row[team_member_col])) or 
            ( _check_finished(row[status_col]) and not _check_date(row[date_col])) or 
            (_check_not_started(row[status_col]))):
            return

        member_data = self.all_data[row[1]]
        progress_list = member_data.data[row[2]]
        progress_list.append(row[0])


    # Add server data that is in progress, waiting for PR, or finished that day
    def _add_server_data(self, row) -> None:
        task_name_col = 1
        server_team_member_col = 5
        server_status_col = 6
        server_date_col = 7
        client_team_member_col = 9
        client_status_col = 10
        client_date_col = 11

        is_invalid_server = (not _check_member(row[server_team_member_col]) or 
            (_check_finished(row[server_status_col]) and not _check_date(row[server_date_col])) or 
            (_check_not_started(row[server_status_col])))
        
        is_invalid_client = (not _check_member(row[client_team_member_col]) or
            (_check_finished(row[client_status_col]) and not _check_date(row[client_date_col])) or
            (_check_not_started(row[client_status_col])))

        if not is_invalid_server:
            member_data = self.all_data[row[server_team_member_col]]
            progress_list = member_data.data[row[server_status_col]]
            progress_list.append(f"[サーバー] {row[task_name_col]}")

        if not is_invalid_client:
            member_data = self.all_data[row[client_team_member_col]]
            progress_list = member_data.data[row[client_status_col]]
            progress_list.append(f"[クライアント] {row[task_name_col]}")


    # Add dialog data 
    def add_dialog_data(self, data) -> None:
        for d in data:
            self._add_dialog_data(d)

    
    # Add server data
    def add_server_data(self, data) -> None:
        for d in data:
            self._add_server_data(d)


    def to_string(self) -> str:
        res = f"*{_get_today()} 進捗情報：*\n\n\n"
        for key, value in self.all_data.items():
            res += f"{key}\n\n"
            for embedKey, embedValue in value.data.items():
                if len(embedValue) == 0:
                    continue
                res += "```"
                res += f"{embedKey}\n"
                for task in embedValue:
                    res += f"{Constants.INDENT}{task}\n"
                res += "```"
                res += "\n"
            res += "\n\n"    
        return res
        