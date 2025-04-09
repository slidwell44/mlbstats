# config/endpoints.py

import typing as t

from pydantic import BaseModel, Field


class ParamSpec(BaseModel):
    type: str
    default: t.Optional[t.Any]
    leading_slash: bool = Field(default=False)
    trailing_slash: bool = Field(default=False)
    required: bool = Field(default=False)
    True_str: t.Optional[str] = Field(default=None)
    False_str: t.Optional[str] = Field(default=None)


class EndpointConfig(BaseModel):
    url: str
    path_params: dict[str, ParamSpec]
    query_params: list[str] = Field(default_factory=list)
    required_params: list[list[str]] = Field(default_factory=list)
    note: t.Optional[str] = Field(default=None)


BASE_URL = "https://statsapi.mlb.com/api/"

ENDPOINTS: dict[str, EndpointConfig] = {
    "attendance": EndpointConfig(
        url=BASE_URL + "{ver}/attendance",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "teamId",
            "leagueId",
            "season",
            "date",
            "leagueListId",
            "gameType",
            "fields",
        ],
        required_params=[["teamId"], ["leagueId"], ["leagueListid"]],
    ),
    "awards": EndpointConfig(
        url=BASE_URL + "{ver}/awards{awardId}{recipients}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "awardId": ParamSpec(
                type="str",
                default=None,
                leading_slash=True,
                trailing_slash=False,
                required=False,
            ),
            "recipients": ParamSpec(
                type="bool",
                default=True,
                True_str="/recipients",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
        },
        query_params=["sportId", "leagueId", "season", "hydrate", "fields"],
        required_params=[[]],
        note="Call awards endpoint with no parameters to return a list of awardIds.",
    ),
    "conferences": EndpointConfig(
        url=BASE_URL + "{ver}/conferences",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["conferenceId", "season", "fields"],
        required_params=[[]],
    ),
    "divisions": EndpointConfig(
        url=BASE_URL + "{ver}/divisions",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["divisionId", "leagueId", "sportId", "season"],
        required_params=[[]],
        note="Call divisions endpoint with no parameters to return a list of divisions.",
    ),
    "draft": EndpointConfig(
        url=BASE_URL + "{ver}/draft{prospects}{year}{latest}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "prospects": ParamSpec(
                type="bool",
                default=False,
                True_str="/prospects",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
            "year": ParamSpec(
                type="str",
                default="",
                leading_slash=True,
                trailing_slash=False,
                required=False,
            ),
            "latest": ParamSpec(
                type="bool",
                default=False,
                True_str="/latest",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
        },
        query_params=[
            "limit",
            "fields",
            "round",
            "name",
            "school",
            "state",
            "country",
            "position",
            "teamId",
            "playerId",
            "bisPlayerId",
        ],
        required_params=[[]],
        note='No query parameters are honored when "latest" endpoint is queried (year is still required). Prospects and Latest cannot be used together.',
    ),
    "game": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/live",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1.1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "hydrate", "fields"],
        required_params=[[]],
    ),
    "game_diff": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/live/diffPatch",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1.1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["startTimecode", "endTimecode"],
        required_params=[["startTimecode", "endTimecode"]],
    ),
    "game_timestamps": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/live/timestamps",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1.1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[],
        required_params=[[]],
    ),
    "game_changes": EndpointConfig(
        url=BASE_URL + "{ver}/game/changes",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["updatedSince", "sportId", "gameType", "season", "fields"],
        required_params=[["updatedSince"]],
    ),
    "game_contextMetrics": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/contextMetrics",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "game_winProbability": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/winProbability",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
        note="If you only want the current win probability for each team, try the game_contextMetrics endpoint instead.",
    ),
    "game_boxscore": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/boxscore",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "game_content": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/content",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["highlightLimit"],
        required_params=[[]],
    ),
    "game_color": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/color",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "game_color_diff": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/color/diffPatch",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["startTimecode", "endTimecode"],
        required_params=[["startTimeCode", "endTimeCode"]],
    ),
    "game_color_timestamps": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/feed/color/timestamps",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[],
        required_params=[[]],
    ),
    "game_linescore": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/linescore",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "game_playByPlay": EndpointConfig(
        url=BASE_URL + "{ver}/game/{gamePk}/playByPlay",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "game_uniforms": EndpointConfig(
        url=BASE_URL + "{ver}/uniforms/game",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["gamePks", "fields"],
        required_params=[["gamePks"]],
    ),
    "gamePace": EndpointConfig(
        url=BASE_URL + "{ver}/gamePace",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "season",
            "teamIds",
            "leagueIds",
            "leagueListId",
            "sportId",
            "gameType",
            "startDate",
            "endDate",
            "venueIds",
            "orgType",
            "includeChildren",
            "fields",
        ],
        required_params=[["season"]],
    ),
    "highLow": EndpointConfig(
        url=BASE_URL + "{ver}/highLow/{orgType}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "orgType": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[
            "statGroup",
            "sortStat",
            "season",
            "gameType",
            "teamId",
            "leagueId",
            "sportIds",
            "limit",
            "fields",
        ],
        required_params=[["sortStat", "season"]],
        note="Valid values for orgType parameter: player, team, division, league, sport, types.",
    ),
    "homeRunDerby": EndpointConfig(
        url=BASE_URL + "{ver}/homeRunDerby/{gamePk}{bracket}{pool}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "bracket": ParamSpec(
                type="bool",
                default=False,
                True_str="/bracket",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
            "pool": ParamSpec(
                type="bool",
                default=False,
                True_str="/pool",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
        },
        query_params=["fields"],
        required_params=[[]],
    ),
    "league": EndpointConfig(
        url=BASE_URL + "{ver}/league",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["sportId", "leagueIds", "seasons", "fields"],
        required_params=[["sportId"], ["leagueIds"]],
    ),
    "league_allStarBallot": EndpointConfig(
        url=BASE_URL + "{ver}/league/{leagueId}/allStarBallot",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "leagueId": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "fields"],
        required_params=[["season"]],
    ),
    "league_allStarWriteIns": EndpointConfig(
        url=BASE_URL + "{ver}/league/{leagueId}/allStarWriteIns",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "leagueId": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "fields"],
        required_params=[["season"]],
    ),
    "league_allStarFinalVote": EndpointConfig(
        url=BASE_URL + "{ver}/league/{leagueId}/allStarFinalVote",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "leagueId": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "fields"],
        required_params=[["season"]],
    ),
    "people": EndpointConfig(
        url=BASE_URL + "{ver}/people",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["personIds", "hydrate", "fields"],
        required_params=[["personIds"]],
    ),
    "people_changes": EndpointConfig(
        url=BASE_URL + "{ver}/people/changes",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["updatedSince", "fields"],
        required_params=[[]],
    ),
    "people_freeAgents": EndpointConfig(
        url=BASE_URL + "{ver}/people/freeAgents",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "leagueId": ParamSpec(
                type="str",
                default="",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["order", "hydrate", "fields"],
        required_params=[[]],
    ),
    "person": EndpointConfig(
        url=BASE_URL + "{ver}/people/{personId}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "personId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["hydrate", "fields"],
        required_params=[[]],
    ),
    "person_stats": EndpointConfig(
        url=BASE_URL + "{ver}/people/{personId}/stats/game/{gamePk}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "personId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "gamePk": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["fields"],
        required_params=[[]],
        note='Specify "current" instead of a gamePk for a player\'s current game stats.',
    ),
    "jobs": EndpointConfig(
        url=BASE_URL + "{ver}/jobs",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["jobType", "sportId", "date", "fields"],
        required_params=[["jobType"]],
    ),
    "jobs_umpires": EndpointConfig(
        url=BASE_URL + "{ver}/jobs/umpires",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["sportId", "date", "fields"],
        required_params=[[]],
    ),
    "jobs_umpire_games": EndpointConfig(
        url=BASE_URL + "{ver}/jobs/umpires/games/{umpireId}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "umpireId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "fields"],
        required_params=[["season"]],
    ),
    "jobs_datacasters": EndpointConfig(
        url=BASE_URL + "{ver}/jobs/datacasters",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["sportId", "date", "fields"],
        required_params=[[]],
    ),
    "jobs_officialScorers": EndpointConfig(
        url=BASE_URL + "{ver}/jobs/officialScorers",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["timecode", "fields"],
        required_params=[[]],
    ),
    "schedule": EndpointConfig(
        url=BASE_URL + "{ver}/schedule",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "scheduleType",
            "eventTypes",
            "hydrate",
            "teamId",
            "leagueId",
            "sportId",
            "gamePk",
            "gamePks",
            "venueIds",
            "gameTypes",
            "date",
            "startDate",
            "endDate",
            "opponentId",
            "fields",
            "season",
        ],
        required_params=[["sportId"], ["gamePk"], ["gamePks"]],
    ),
    "schedule_tied": EndpointConfig(
        url=BASE_URL + "{ver}/schedule/games/tied",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["gameTypes", "season", "hydrate", "fields"],
        required_params=[["season"]],
    ),
    "schedule_postseason": EndpointConfig(
        url=BASE_URL + "{ver}/schedule/postseason",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "gameTypes",
            "seriesNumber",
            "teamId",
            "sportId",
            "season",
            "hydrate",
            "fields",
        ],
        required_params=[[]],
    ),
    "schedule_postseason_series": EndpointConfig(
        url=BASE_URL + "{ver}/schedule/postseason/series",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "gameTypes",
            "seriesNumber",
            "teamId",
            "sportId",
            "season",
            "fields",
        ],
        required_params=[[]],
    ),
    "schedule_postseason_tuneIn": EndpointConfig(
        url=BASE_URL + "{ver}/schedule/postseason/tuneIn",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["teamId", "sportId", "season", "hydrate", "fields"],
        required_params=[[]],
        note="The schedule_postseason_tuneIn endpoint appears to return no data.",
    ),
    "seasons": EndpointConfig(
        url=BASE_URL + "{ver}/seasons{all}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "all": ParamSpec(
                type="bool",
                default=False,
                True_str="/all",
                False_str="",
                leading_slash=False,
                trailing_slash=False,
                required=False,
            ),
        },
        query_params=["season", "sportId", "divisionId", "leagueId", "fields"],
        required_params=[["sportId"], ["divisionId"], ["leagueId"]],
        note='Include "all" parameter with value of True to query all seasons. The divisionId and leagueId parameters are supported when "all" is used.',
    ),
    "season": EndpointConfig(
        url=BASE_URL + "{ver}/seasons/{seasonId}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "seasonId": ParamSpec(
                type="str",
                default=False,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["sportId", "fields"],
        required_params=[["sportId"]],
    ),
    "sports": EndpointConfig(
        url=BASE_URL + "{ver}/sports",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["sportId", "fields"],
        required_params=[[]],
    ),
    "sports_players": EndpointConfig(
        url=BASE_URL + "{ver}/sports/{sportId}/players",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "sportId": ParamSpec(
                type="str",
                default="1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "gameType", "fields"],
        required_params=[["season"]],
    ),
    "standings": EndpointConfig(
        url=BASE_URL + "{ver}/standings",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "leagueId",
            "season",
            "standingsTypes",
            "date",
            "hydrate",
            "fields",
        ],
        required_params=[["leagueId"]],
    ),
    "stats": EndpointConfig(
        url=BASE_URL + "{ver}/stats",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "stats",
            "playerPool",
            "position",
            "teamId",
            "leagueId",
            "limit",
            "offset",
            "group",
            "gameType",
            "season",
            "sportIds",
            "sortStat",
            "order",
            "hydrate",
            "fields",
            "personId",
            "metrics",
            "startDate",
            "endDate",
        ],
        required_params=[["stats", "group"]],
        note="If no limit is specified, the response will be limited to 50 records.",
    ),
    "stats_leaders": EndpointConfig(
        url=BASE_URL + "{ver}/stats/leaders",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "leaderCategories",
            "playerPool",
            "leaderGameTypes",
            "statGroup",
            "season",
            "leagueId",
            "sportId",
            "hydrate",
            "limit",
            "fields",
            "statType",
        ],
        required_params=[["leaderCategories"]],
        note="If excluding season parameter to get all time leaders, include statType=statsSingleSeason or you will likely not get any results.",
    ),
    "stats_streaks": EndpointConfig(
        url=BASE_URL + "{ver}/stats/streaks",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "streakType",
            "streakSpan",
            "gameType",
            "season",
            "sportId",
            "limit",
            "hydrate",
            "fields",
        ],
        required_params=[["streakType", "streakSpan", "season", "sportId", "limit"]],
        note='Valid streakType values: "hittingStreakOverall" "hittingStreakHome" "hittingStreakAway" "onBaseOverall" "onBaseHome" "onBaseAway". Valid streakSpan values: "career" "season" "currentStreak" "currentStreakInSeason" "notable" "notableInSeason".',
    ),
    "teams": EndpointConfig(
        url=BASE_URL + "{ver}/teams",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "season",
            "activeStatus",
            "leagueIds",
            "sportId",
            "sportIds",
            "gameType",
            "hydrate",
            "fields",
        ],
        required_params=[[]],
    ),
    "teams_history": EndpointConfig(
        url=BASE_URL + "{ver}/teams/history",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["teamIds", "startSeason", "endSeason", "fields"],
        required_params=[["teamIds"]],
    ),
    "teams_stats": EndpointConfig(
        url=BASE_URL + "{ver}/teams/stats",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "season",
            "sportIds",
            "group",
            "gameType",
            "stats",
            "order",
            "sortStat",
            "fields",
            "startDate",
            "endDate",
        ],
        required_params=[["season", "group", "stats"]],
        note="Use meta('statGroups') to look up valid values for group, and meta('statTypes') for valid values for stats.",
    ),
    "teams_affiliates": EndpointConfig(
        url=BASE_URL + "{ver}/teams/affiliates",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["teamIds", "sportId", "season", "hydrate", "fields"],
        required_params=[["teamIds"]],
    ),
    "team": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "sportId", "hydrate", "fields"],
        required_params=[[]],
    ),
    "team_alumni": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/alumni",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "group", "hydrate", "fields"],
        required_params=[["season", "group"]],
    ),
    "team_coaches": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/coaches",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["season", "date", "fields"],
        required_params=[[]],
    ),
    "team_personnel": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/personnel",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["date", "fields"],
        required_params=[[]],
    ),
    "team_leaders": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/leaders",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[
            "leaderCategories",
            "season",
            "leaderGameTypes",
            "hydrate",
            "limit",
            "fields",
        ],
        required_params=[["leaderCategories", "season"]],
    ),
    "team_roster": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/roster",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=["rosterType", "season", "date", "hydrate", "fields"],
        required_params=[[]],
    ),
    "team_stats": EndpointConfig(
        url=BASE_URL + "{ver}/teams/{teamId}/stats",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "teamId": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[
            "season",
            "group",
            "gameType",
            "stats",
            "sportIds",
            "sitCodes",
            "fields",
        ],
        required_params=[["season", "group"]],
        note="Use meta('statGroups') to look up valid values for group, meta('statTypes') for valid values for stats, and meta('situationCodes') for valid values for sitCodes. Use sitCodes with stats=statSplits.",
    ),
    "team_uniforms": EndpointConfig(
        url=BASE_URL + "{ver}/uniforms/team",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["teamIds", "season", "fields"],
        required_params=[["teamIds"]],
    ),
    "transactions": EndpointConfig(
        url=BASE_URL + "{ver}/transactions",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=[
            "teamId",
            "playerId",
            "date",
            "startDate",
            "endDate",
            "sportId",
            "fields",
        ],
        required_params=[["teamId"], ["playerId"], ["date"], ["startDate", "endDate"]],
    ),
    "venue": EndpointConfig(
        url=BASE_URL + "{ver}/venues",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            )
        },
        query_params=["venueIds", "season", "hydrate", "fields"],
        required_params=[["venueIds"]],
    ),
    "meta": EndpointConfig(
        url=BASE_URL + "{ver}/{type}",
        path_params={
            "ver": ParamSpec(
                type="str",
                default="v1",
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
            "type": ParamSpec(
                type="str",
                default=None,
                leading_slash=False,
                trailing_slash=False,
                required=True,
            ),
        },
        query_params=[],
        required_params=[[]],
        note="The meta endpoint is used to retrieve values to be used within other API calls. Available types: awards, baseballStats, eventTypes, gameStatus, gameTypes, hitTrajectories, jobTypes, languages, leagueLeaderTypes, logicalEvents, metrics, pitchCodes, pitchTypes, platforms, positions, reviewReasons, rosterTypes, scheduleEventTypes, situationCodes, sky, standingsTypes, statGroups, statTypes, windDirection.",
    ),
    # v1/analytics and v1/game/{gamePk}/guids endpoints (statcast data) require authentication.
}
