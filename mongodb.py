import sys, urllib.parse, urllib.request, json
from pymongo import MongoClient

try:
	# use urllib to grab json
	url = "https://0.0.0.0:5000/"
	urlHandle = urllib.parse.urlparse(url)
	response = urllib.request.urlopen(urlHandle.geturl())
	encoding = response.info().get_content_charset("utf-8")
	payload = response.read().decode(encoding)
	jsonStream = json.loads(payload)
except:
	e = sys.exc_info()[0]
	print("error: {}".format(e))

# use pymongo to write json to mongodb on localhost
client = MongoClient()
db = client.module4
collection = db.payload

for element in jsonStream:
	collection.insert_one(element)
	print("Inserted elementID: ", element["id"])

client.close()
