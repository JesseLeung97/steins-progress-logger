class Status:
    NotStarted = "未着手"
    InProgress = "進行中"
    WaitingForPR = "PR待ち"
    Finished = "完了"


# Contain a list of tasks for each team member for each progress interval
class ProgressData:
    def __init__(self) -> None:
        self.data = {
            Status.NotStarted: [],
            Status.InProgress: [],
            Status.WaitingForPR: [],
            Status.Finished: []
        }