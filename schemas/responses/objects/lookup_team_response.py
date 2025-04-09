# schemas/lookup_team_response.py

from pydantic import BaseModel, Field


class Team(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    teamCode: str = Field(...)
    fileCode: str = Field(...)
    teamName: str = Field(...)
    locationName: str = Field(...)
    shortName: str = Field(...)


class LookupTeamResponse(BaseModel):
    data: list[Team] = Field(default_factory=list)
