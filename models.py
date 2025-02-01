from pydantic import BaseModel, Field
from typing import List, Optional


class Character(BaseModel):
    id: int
    name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0, le=120)
    occupation: str = Field(..., max_length=100)
    catchphrase: Optional[str] = Field(None, max_length=100)
    family_id: Optional[int] = None


class Song(BaseModel):
    id: int
    title: str = Field(..., max_length=100)
    lyrics: str
    character_id: Optional[int] = None
    episode: str = Field(..., max_length=100)


class Family(BaseModel):
    id: int
    name: str = Field(..., max_length=100)
    members: List[int] = []
    description: Optional[str] = Field(None, max_length=200)
