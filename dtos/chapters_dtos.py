class ChapterRequestDto(BaseModel):
    name: str
    text: str
    rating : Optional[float]

class ChapterRatingRequest(BaseModel):
    user_id : str
    course_id : str
    chapter_id : str
    rating: bool  # True for positive, False for negative

class ChapterResponse(BaseModel):
    name: str
    text: str
    rating: Optional[float]
    num_ratings: int