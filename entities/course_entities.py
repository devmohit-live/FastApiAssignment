class Course(BaseModel):
    _id : str
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]


class Chapter(BaseModel):
    _id : str
    name: str
    text: str
    rating : Optional[float]