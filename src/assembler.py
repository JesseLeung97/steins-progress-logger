from src.team_members import TeamMembers
from src.progress_data import ProgressData
from datetime import datetime


# Only add tasks which have been updated today
def check_date(listed_date: str) -> bool:
    today = datetime.today().strftime("%Y/%m/%d")
    if not listed_date.__eq__(today):
        return False
    return True


# Gather progress data for each team member then convert to a message string
class DataCollector: 
    def __init__(self) -> None:
        self.all_data = {
            TeamMembers.Simon: ProgressData(),
            TeamMembers.Andreas: ProgressData(),
            TeamMembers.Tom: ProgressData(),
            TeamMembers.Jesse: ProgressData()
        }


    def _add_data(self, row) -> None:
        if not check_date(row[3]):
            return

        member_data = self.all_data[row[1]]
        progress_list = member_data.data[row[2]]
        progress_list.append(row[0])


    def add_data(self, data) -> None:
        for d in data:
            self._add_data(d)


    def to_string(self) -> str:
        res = ""
        for key, value in self.all_data.items():
            res += f"{key}\n\n"
            for embedKey, embedValue in value.data.items():
                if len(embedValue) == 0:
                    continue
                
                res += f"{embedKey}\n"
                for task in embedValue:
                    res += f"    {task}\n"
                res += "\n"
            res += "-----\n\n"    
        return res
        