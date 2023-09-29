import json

from modules.csv_reader import takeBooks
from modules.json_reader import genJson

books = takeBooks()
genJson(books)

def count_books_per_user(users):
    user_book_counts = {}

    for user in users:
        user_name = user.get("name", "Unknown")
        books = user.get("books", [])
        book_count = len(books)
        user_book_counts[user_name] = book_count

    return user_book_counts



with open("example.json", "r") as f:
    users = json.load(f)


user_book_counts = count_books_per_user(users)


for user, count in user_book_counts.items():
    print(f"{user} имеет {count} книг")
