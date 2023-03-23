from entities.course_entities import *
from dtos.course_dtos import *
from repository.course_repository import *
from repository.course_repository import *
from utils.id_utils import *


def get_course_overview(course_id :str) ->CourseOverview:
    # check if the course exists
    course = get_course_by_id(course_id)
    if course is None:
        return None

    course = dict(course)
    ratings = get_course_rating(course_id)
    no_of_chapters = len(course.get('chapters'))
    no_of_ratings = len(ratings)

    if no_of_ratings == 0:
        avg_rating = 0
    else:
        rating_sum = 0
        for rating in ratings:
            if dict(rating).get('rating') == True:
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