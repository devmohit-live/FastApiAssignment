import pymongo
import certifi
from utils.providers_utils import get_mongo_client
from entities.course_entities import *

client = client = get_mongo_client()

db = client["courseDb"]
course_collection = db["courses"]

def add_course(course : Course):
    course_id = get_course_id()
    chapters = []
    for chapter in course.chapters:
        chapters.append({"_id": get_chapter_id(course_id),"name": chapter.name, "text": chapter.text})
    doc =  {
            "_id": course_id,
            "name":course.name,
            "description":course.description,
            "domain":course.domain,
            "date":course.date,
            "chapters": chapters
            }

    response = course_collection.insert_one(doc)
    return response.inserted_id

def get_all():
    response = course_collection.find({})
    return list(response)

def get_course_by_id(course_id):
    response = course_collection.find_one({"_id" : str(course_id)})
    print('Db course',response)
    return response

def get_courses_by_domain(domain):
    response = course_collection.find({"domain" : domain})
    return list(response)


def get_chapter_by_id(course_id, chapter_id):
    course = get_course_by_id(course_id)
    chapters = dict(course).get('chapters')
    print("Chapters got is ", chapters)
    for chapter in chapters :
        if dict(chapter).get('_id') == chapter_id:
            return chapter
    else:
        return  None
