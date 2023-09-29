import json
import config as config

with open(config.JSON_FILE_PATH, "r") as f:
    users = json.loads(f.read())


def genJson(books):
    booksCount = len(books)
    userCount = len(users)
    booksforone = booksCount // userCount
    remaining_books = booksCount % userCount

    lastIndex = 0
    data = []

    for user in users:
        bbooks = []
        for i in range(booksforone):
            bbooks.append(books[lastIndex])
            lastIndex += 1

        if remaining_books > 0:
            bbooks.append(books[lastIndex])
            lastIndex += 1
            remaining_books -= 1

        usr_json = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": bbooks
        }
        data.append(usr_json)

    with open("example.json", "w") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


