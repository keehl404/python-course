import os

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


BOOKS_CSV_FILE = get_path("books.csv")
USERS_JSON_FILE = get_path("users.json")
