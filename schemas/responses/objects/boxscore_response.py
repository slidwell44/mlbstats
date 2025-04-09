import typing as t

from pydantic import BaseModel, Field


class BoxscoreBatter(BaseModel):
    namefield: str = Field(
        ...,
        description="Display field for the batter, including name and extra details",
    )
    ab: str = Field(..., description="At bats")
    r: str = Field(..., description="Runs scored")
    h: str = Field(..., description="Hits")
    doubles: str = Field(..., description="Doubles hit")
    triples: str = Field(..., description="Triples hit")
    hr: str = Field(..., description="Home runs")
    rbi: str = Field(..., description="Runs batted in")
    sb: str = Field(..., description="Stolen bases")
    bb: str = Field(..., description="Base on balls (walks)")
    k: str = Field(..., description="Strikeouts")
    lob: str = Field(..., description="Left on base")
    avg: str = Field(..., description="Batting average")
    ops: str = Field(..., description="On-base plus slugging")
    personId: int = Field(..., description="Unique player identifier")
    substitution: bool = Field(
        ..., description="Indicator whether the batter was a substitution"
    )
    note: str = Field(..., description="Additional notes for this batter")
    name: str = Field(..., description="Batter's name")
    position: str = Field(..., description="Position abbreviation")
    obp: str = Field(..., description="On-base percentage")
    slg: str = Field(..., description="Slugging percentage")
    battingOrder: str = Field(..., description="Batting order position")


class BoxscorePitcher(BaseModel):
    namefield: str = Field(
        ...,
        description="Display field for the pitcher, including name and extra details",
    )
    ip: str = Field(..., description="Innings pitched")
    h: str = Field(..., description="Hits allowed")
    r: str = Field(..., description="Runs allowed")
    er: str = Field(..., description="Earned runs")
    bb: str = Field(..., description="Walks allowed")
    k: str = Field(..., description="Strikeouts")
    hr: str = Field(..., description="Home runs allowed")
    era: str = Field(..., description="Earned run average")
    p: str = Field(..., description="Pitch count or number of pitches thrown")
    s: str = Field(..., description="Strikes thrown")
    name: str = Field(..., description="Pitcher's name")
    personId: int = Field(..., description="Unique pitcher identifier")
    note: str = Field(..., description="Additional notes for this pitcher")


class BoxscoreResponse(BaseModel):
    gameId: int = Field(..., description="Game ID from game data")
    teamInfo: dict[str, t.Any] = Field(..., description="Metadata for each team")
    playerInfo: dict[str, t.Any] = Field(..., description="Player information data")
    away: dict[str, t.Any] = Field(..., description="Away team boxscore data")
    home: dict[str, t.Any] = Field(..., description="Home team boxscore data")
    awayBatters: list[BoxscoreBatter] = Field(
        default_factory=list, description="list of batters for the away team"
    )
    homeBatters: list[BoxscoreBatter] = Field(
        default_factory=list, description="list of batters for the home team"
    )
    awayBattingTotals: t.Optional[BoxscoreBatter] = Field(
        None, description="Batting totals for the away team"
    )
    homeBattingTotals: t.Optional[BoxscoreBatter] = Field(
        None, description="Batting totals for the home team"
    )
    awayBattingNotes: list[str] = Field(
        default_factory=list, description="Notes related to the away team batting"
    )
    homeBattingNotes: list[str] = Field(
        default_factory=list, description="Notes related to the home team batting"
    )
    awayPitchers: list[BoxscorePitcher] = Field(
        default_factory=list, description="list of pitchers for the away team"
    )
    homePitchers: list[BoxscorePitcher] = Field(
        default_factory=list, description="list of pitchers for the home team"
    )
    awayPitchingTotals: t.Optional[BoxscorePitcher] = Field(
        None, description="Pitching totals for the away team"
    )
    homePitchingTotals: t.Optional[BoxscorePitcher] = Field(
        None, description="Pitching totals for the home team"
    )
    gameBoxInfo: list[str] = Field(
        default_factory=list, description="Additional game boxscore information"
    )
