from typing import List, Optional
from pydantic import BaseModel

class CourseRequestDto(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]


class CourseResponseDto(BaseModel):
    _id : str
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]


class CourseListFilter(BaseModel):
    domain: Optional[str]


class CourseListSort(BaseModel):
    sort_by: str  # "alphabetical", "date", or "rating"


class CourseList(BaseModel):
    courses: List[Course]


class CourseListResponse(BaseModel):
    courses: List[Course]
    count: int


class CourseOverview(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    num_chapters: int
    average_rating: Optional[float]