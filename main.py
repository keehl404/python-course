import json
from csv import DictReader
from files import BOOKS_CSV_FILE
from files import USERS_JSON_FILE

books = []
users = []

with open(BOOKS_CSV_FILE) as f:
    for book in DictReader(f):
        books.append({
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        })

with open(USERS_JSON_FILE, "r") as f:
    for user in json.loads(f.read()):
        users.append(
            {"name": user["name"],
             "gender": user["gender"],
             "address": user["address"],
             "age": int(user["age"]),
             "books": []})


def add_books(books, users):
    user_counter = 0

    for book in books:
        users[user_counter]["books"].append(book)
        user_counter = user_counter + \
                       1 if user_counter < (len(users) - 1) else 0


result_data = add_books(books, users)

with open("result.json", "w") as f:
    json.dump(users, f, indent=4)
