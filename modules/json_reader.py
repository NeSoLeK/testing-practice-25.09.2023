import json
import modules.config as config


with open(config.JSON_FILE_PATH, "r") as f:
    users = json.loads(f.read())



def genJson(books):

	booksCount = len(books)
	userCount = len(users)
	booksforone = booksCount // userCount


	lastIndex = 0
	data = []
	
	for user in users:
		bbooks = []
		try:
			for i in range(lastIndex, lastIndex+booksforone):
				bbooks.append(books[i])
				lastIndex += 1
		except:
			for i in range(lastIndex, lastIndex+booksCount%userCount):
				bbooks.append(books[i])
				lastIndex += 1
			
			

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


