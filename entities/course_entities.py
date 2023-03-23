from typing import List, Optional
from pydantic import BaseModel

class Chapter(BaseModel):
    _id : str
    name: str
    text: str
    rating : Optional[float]

class Course(BaseModel):
    _id : str
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
