from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/')
db = client.app
collection = db.app_collection

@app.route('/')
def index():
    collection.insert_one({'name': 'TD5'})
    data = collection.find_one()
    with open("src/file.txt", "r") as f:
        msg = f.read()
    return f"{str(data)}<br>{msg}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
