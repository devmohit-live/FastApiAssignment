from http.client import HTTPException
from fastapi import FastAPI
from entities.course_entities import *
from dtos.course_dtos import *
from repository.course_repository import *
from repository.course_repository import *
app = FastAPI()



#Get all courses
@app.get("/courses", response_model=CourseListResponse)
async def get_courses(
        domain: Optional[str] = None, sort_by: str = "name"
):
    filtered_courses = []
    if domain:
        filtered_courses = get_courses_by_domain(domain)
    else :
        filtered_courses = get_all()


    if sort_by == "name":
        filtered_courses.sort(key=lambda c: dict(c).get('name'))
    elif sort_by == "date":
        filtered_courses.sort(key=lambda c: dict(c).get('date'), reverse=True)
    elif sort_by == "rating":
        filtered_courses.sort(key=lambda c: dict(c).get('name'))
        # Add rating sorting logic here
    return {"courses": filtered_courses, "count": len(filtered_courses)}



#Get Chapter Information
@app.get("/courses/{course_id}/chapters/{chapter_id}", response_model=ChapterResponse)
async def get_chapter_overview(course_id: str, chapter_id: str):
    chapter = get_chapter_by_id(course_id, chapter_id)
    if chapter == None:
        return None
    ratings = get_chapter_ratings(chapter_id);
    no_of_ratings = len(ratings)

    if no_of_ratings == 0:
        avg_rating = 0
    else:
        rating_sum = 0
        for rating in ratings:
            if dict(rating).get('rating') == True :
                rating_sum = rating_sum + 1

        avg_rating = (rating_sum / no_of_ratings)

    chapter = dict(chapter)
    return { "name": chapter.get('name'),
             "text": chapter.get('text'),
             "rating": avg_rating,
             "num_ratings": no_of_ratings}



#Rate Chapter
@app.post("/courses/{course_id}/rate_chapter/")
def rate_chapter(course_id : str, rating_req: ChapterRatingRequest):
    # check if the course exists
    chapter = get_chapter_by_id(course_id, rating_req.chapter_id)
    if chapter == None:
        raise HTTPException(status_code=404, detail="Course not found")
    rating_req
    add_chapter_rating(rating_req)


    return {"message": "Chapter rating added successfully" }



@app.get("/courses/{course_id}/overview/", response_model=CourseOverview)
def get_course_overview(course_id: str) -> CourseOverview:
    # check if the course exists
    course = get_course_by_id(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")


    course = dict(course)
    ratings = get_course_rating(course_id)
    no_of_chapters = len(course.get('chapters'))
    no_of_ratings = len(ratings)
    rating_sum = 0
    for rating in ratings:
        if dict(rating).get('rating') == True :
            rating_sum = rating_sum + 1

    avg_rating = (rating_sum / no_of_ratings)

    return CourseOverview(
        name=course.get('name'),
        date=course.get('date'),
        description=course.get('description'),
        domain=course.get('domain'),
        num_chapters=no_of_chapters,
        average_rating=avg_rating
    )