# utils/team_leaders.py

from datetime import datetime
import typing as t

import statsapi as mlb


def lookup_team(
    teamId, leaderCategories, season=datetime.now().year, leaderGameTypes="R", limit=10
):
    res: dict[str, t.Any] = mlb.team_leaders(
        teamId=teamId,
        leaderCategories=leaderCategories,
        season=season,
        leaderGameTypes=leaderGameTypes,
        limit=limit,
    )
