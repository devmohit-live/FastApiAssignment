import pymongo
import certifi

client = client = get_mongo_client()

db = client["courseDb"]
chapter_rating_collection = db["chapterRatings"]


def add_chapter_rating(chapter_rating: ChapterRating):
    chapter_rating_collection.insert_one(dict(chapter_rating))


def get_chapter_ratings(chapter_id):
    return list(chapter_rating_collection.find({"chapter_id" : chapter_id}))


def get_course_rating(course_id):
    return list(chapter_rating_collection.find({"course_id" : course_id}))