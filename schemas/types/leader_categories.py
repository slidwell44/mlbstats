from enum import Enum


class LeaderCategory(str, Enum):
    battingAverage = "avg"
    onBasePlusSlugging = "ops"
    runsBattedIn = "rbi"
