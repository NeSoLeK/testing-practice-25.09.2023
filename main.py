from modules.csv_reader import takeBooks
from modules.json_reader import genJson

books = takeBooks()
genJson(books)