import json
import csv
import config as config
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def takeBooks():
    with open(config.CSV_FILE_PATH, newline='') as f:
        reader = csv.reader(f)

        # Извлечение заголовка
        header = next(reader)
        books = []

        for row in reader:
            books.append(dict(zip(header, row)))

        return books


def generate_user_data(users, books,current_user_index=0):
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

    return data


def add_book_to_user(user_data, user_index, new_book):
    user_data[user_index]["books"].append(new_book)


def update_json_file(user_data):
    try:
        with open("example5.json", "w") as f:
            s = json.dumps(user_data, indent=4)
            f.write(s)
    except Exception as e:
        print(f"JSON ERROR: {str(e)}")



class BookHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('books.csv'):
            print(f"File {event.src_path} has been modified.")
            users = json.load(open(config.JSON_FILE_PATH, "r"))
            books = takeBooks()
            user_data = generate_user_data(users, books,current_user_index=0)
            update_json_file(user_data)
            print("File 'books.json' has been modified and JSON updated.")

def count_books_per_user(users):
            user_book_counts = {}

            for user in users:
                user_name = user.get("name", "Unknown")
                books = user.get("books", [])
                book_count = len(books)
                user_book_counts[user_name] = book_count

            return user_book_counts

def main():
    event_handler = BookHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    current_user_index = 0

    try:
        while True:
            users = json.load(open(config.JSON_FILE_PATH, "r"))
            books = takeBooks()
            user_data = generate_user_data(users, books, current_user_index)
            update_json_file(user_data)
            time.sleep(5)

            with open("example5.json", "r") as f:
                users = json.load(f)

            user_book_counts = count_books_per_user(users)

            for user, count in user_book_counts.items():
                print(f"{user} имеет {count} книг")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

