import csv
import config as config
def takeBooks():
    with open(config.CSV_FILE_PATH, newline='') as f:
        reader = csv.reader(f)

        # Извлечение заголовка
        header = next(reader)
        books = []

        # Итерируемся по данным делая из них словари
        for row in reader:
            # print(dict(zip(header, row)))
            books.append(dict(zip(header, row)))

        return books
# with open('../files/users.csv', newline='') as f:
#     reader = DictReader(f)
#
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)