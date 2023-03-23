from typing import List, Optional
from pydantic import BaseModel


class ChapterRequestDto(BaseModel):
    name: str
    text: str

class ChapterRatingRequestDto(BaseModel):
    user_id : str
    chapter_id : str
    rating: bool  # True for positive, False for negative

class ChapterResponse(BaseModel):
    name: str
    text: str
    rating: Optional[float]
    num_ratings: int

class CourseRequestDto(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[ChapterRequestDto]


class CourseResponseDto(BaseModel):
    _id : str
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[ChapterRequestDto]


class CourseListFilter(BaseModel):
    domain: Optional[str]


class CourseListSort(BaseModel):
    sort_by: str  # "alphabetical", "date", or "rating"


class CourseList(BaseModel):
    courses: List[CourseRequestDto]


class CourseListResponse(BaseModel):
    courses: List[CourseRequestDto]
    count: int


class CourseOverview(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    num_chapters: int
    average_rating: Optional[float]