# schemas/responses/schedule_response.py

from typing import Optional

from pydantic import BaseModel, Field


class ScheduleGame(BaseModel):
    game_id: int = Field(..., description="Game primary key")
    game_datetime: str = Field(..., description="Game date and time")
    game_date: str = Field(..., description="Game date")
    game_type: str = Field(..., description="Type of the game")
    status: str = Field(..., description="Detailed game status")
    away_name: str = Field(..., description="Away team name")
    home_name: str = Field(..., description="Home team name")
    away_id: int = Field(..., description="Away team ID")
    home_id: int = Field(..., description="Home team ID")
    doubleheader: bool = Field(
        ..., description="Indicator if the game is part of a doubleheader"
    )
    game_num: int = Field(..., description="Game number in a doubleheader or series")
    home_probable_pitcher: Optional[str] = Field(
        "", description="Home team probable pitcher"
    )
    away_probable_pitcher: Optional[str] = Field(
        "", description="Away team probable pitcher"
    )
    home_pitcher_note: Optional[str] = Field(
        "", description="Pitcher note for home team"
    )
    away_pitcher_note: Optional[str] = Field(
        "", description="Pitcher note for away team"
    )
    away_score: Optional[int] = Field(0, description="Away team score")
    home_score: Optional[int] = Field(0, description="Home team score")
    current_inning: Optional[int] = Field(
        None, description="Current inning if game is in progress"
    )
    inning_state: Optional[str] = Field(
        "", description="Inning state (e.g., top, bottom)"
    )
    venue_id: Optional[int] = Field(None, description="Venue identifier")
    venue_name: Optional[str] = Field(None, description="Venue name")
    national_broadcasts: list[str] = Field(
        default_factory=list, description="Names of national broadcasts"
    )
    series_status: Optional[str] = Field(None, description="Series status")
    winning_team: Optional[str] = Field(
        None, description="Winning team name if game is finished"
    )
    losing_team: Optional[str] = Field(
        None, description="Losing team name if game is finished"
    )
    winning_pitcher: Optional[str] = Field(
        None, description="Winning pitcher's full name"
    )
    losing_pitcher: Optional[str] = Field(
        None, description="Losing pitcher's full name"
    )
    save_pitcher: Optional[str] = Field(None, description="Save pitcher's full name")
    summary: Optional[str] = Field(None, description="A summary of the game info")


class ScheduleResponse(BaseModel):
    data: list[ScheduleGame] = Field(
        default_factory=list, description="List of games in the schedule"
    )
