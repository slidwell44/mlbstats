import typing as t

from pydantic import BaseModel


class GenericResponse(BaseModel):
    data: dict[str, t.Any]
