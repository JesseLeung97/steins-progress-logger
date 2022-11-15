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


    # add data that is in progress, waiting for PR, or finished that day
    def _add_data(self, row) -> None:
        if (not _check_member(row[1])) or ( _check_finished(row[2]) and not _check_date(row[3])) or (_check_not_started(row[2])):
            return

        member_data = self.all_data[row[1]]
        progress_list = member_data.data[row[2]]
        progress_list.append(row[0])


    def add_data(self, data) -> None:
        for d in data:
            self._add_data(d)


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
        