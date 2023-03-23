from http.client import HTTPException
from fastapi import FastAPI
from dtos.course_dtos import *
from services import course_service , overview_service


app = FastAPI()

#Get all courses
@app.get("/courses", response_model=CourseListResponse)
async def get_courses(domain: Optional[str] = None, sort_by: str = "name")-> CourseListResponse:
    return course_service.get_all_courses(domain,sort_by)




#Get Chapter Information
@app.get("/courses/{course_id}/chapters/{chapter_id}", response_model=ChapterResponse)
async def get_chapter_overview(course_id: str, chapter_id: str):
    return course_service.get_chapter_overview(course_id, chapter_id)



#Rate Chapter
@app.post("/courses/{course_id}/rate_chapter/")
def rate_chapter(course_id : str, rating_req: ChapterRatingRequestDto):
    created_resource_id = course_service.rate_chapter(course_id,rating_req)
    if created_resource_id is None :
        raise HTTPException(status_code=404, detail="Course not found")
    else:
        return {"message": f"Chapter rating added successfully ${created_resource_id}" }



@app.get("/courses/{course_id}/overview/", response_model=CourseOverview)
def get_course_overview(course_id: str) -> CourseOverview:
    response =  overview_service.get_course_overview(course_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    else:
        return response