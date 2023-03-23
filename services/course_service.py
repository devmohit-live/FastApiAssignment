from entities.course_entities import *
from dtos.course_dtos import *
from repository.course_repository import *
from repository.course_repository import *
from utils.id_utils import *


def get_all_courses(domain: Optional[str] = None, sort_by: str = "name") -> CourseListResponse:
    filtered_courses = []
    if domain:
        filtered_courses = get_courses_by_domain(domain)
    else:
        filtered_courses = get_all()

    if sort_by == "name":
        filtered_courses.sort(key=lambda c: dict(c).get('name'))
    elif sort_by == "date":
        filtered_courses.sort(key=lambda c: dict(c).get('date'), reverse=True)
    elif sort_by == "rating":
        filtered_courses.sort(key=lambda c: dict(c).get('name'))


    response = CourseListResponse(
        courses=filtered_courses,
        count=len(filtered_courses)
    )

    return response


def get_chapter_overview(course_id: str, chapter_id : str) -> ChapterResponse:
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
            if dict(rating).get('rating') == True:
                rating_sum = rating_sum + 1

        avg_rating = (rating_sum / no_of_ratings)

    chapter = dict(chapter)
    chapter_response = ChapterResponse(
        name=chapter.get('name'),
        text=chapter.get('text'),
        rating=avg_rating,
        num_ratings=no_of_ratings
    )
    return chapter_response



def rate_chapter(course_id : str, chapter_rating_dto : ChapterRatingRequestDto):
    # check if the course exists
    chapter = get_chapter_by_id(course_id, chapter_rating_dto.chapter_id)
    if chapter == None:
        return None
    id = get_rating_id(chapter_rating_dto.chapter_id)
    rating_entity = ChapterRating(
        _id = id,
        user_id=chapter_rating_dto.user_id,
        course_id=course_id,
        chapter_id=chapter_rating_dto.chapter_id,
        rating=chapter_rating_dto.rating
    )
    created_id = add_chapter_rating(rating_entity)
    return created_id

