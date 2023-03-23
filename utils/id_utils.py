from nanoid import  generate
alphabet_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
id_length = 8

def get_course_id() -> str:
    id = 'CS'+ generate(alphabet_set, id_length)
    return str(id)


def get_chapter_id(course_id: str) -> str:
    id =  course_id+'-CH'+ generate(alphabet_set, id_length);
    return str(id)


def get_rating_id(chapter_id:str)->str:
    id = 'CR'+generate(alphabet_set, 12)
    return str(id)