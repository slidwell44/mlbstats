# utils/lookup_team.py

import typing as t

import statsapi as mlb

from schemas.responses import Team, LookupTeamResponse


def lookup_team(
    lookup_value, activeStatus="Y", season=None, sportIds=1
) -> LookupTeamResponse:
    res: dict[str, t.Any] = mlb.lookup_team(
        lookup_value=lookup_value,
        activeStatus=activeStatus,
        season=season,
        sportIds=sportIds,
    )

    return LookupTeamResponse(data=[Team.model_validate(x) for x in res])
