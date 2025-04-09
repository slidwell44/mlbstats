# utils/schedule.py

import typing as t

import statsapi as mlb

from schemas.responses import ScheduleResponse, ScheduleGame


def schedule(
    date=None,
    start_date=None,
    end_date=None,
    team="",
    opponent="",
    sportId=1,
    game_id=None,
    leagueId=None,
    season=None,
    include_series_status=True,
) -> ScheduleResponse:
    res: dict[str, t.Any] = mlb.schedule(
        date=date,
        start_date=start_date,
        end_date=end_date,
        team=team,
        opponent=opponent,
        sportId=sportId,
        game_id=game_id,
        leagueId=leagueId,
        season=season,
        include_series_status=include_series_status,
    )

    return ScheduleResponse(data=[ScheduleGame.model_validate(x) for x in res])
