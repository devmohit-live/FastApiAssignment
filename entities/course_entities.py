from typing import List, Optional
from pydantic import BaseModel

class Chapter(BaseModel):
    _id : str
    name: str
    text: str

class Course(BaseModel):
    _id : str
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]

class ChapterRating(BaseModel):
    _id : str
    user_id : str
    course_id : str
    chapter_id : str
    rating: bool
