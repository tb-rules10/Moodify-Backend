from typing import Type
from pydantic import BaseModel

class EmotionDetector(BaseModel):
    text: str
    class Config:
        orm_mode = True


class EmotionGenre(BaseModel):
    name: str
    emotion: str
    genre: str
    class Config:
        orm_mode = True

