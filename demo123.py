import os

import pymongo as pymongo
from flask import Flask, request, render_template, flash, redirect, url_for, send_file, make_response, jsonify, session



app = Flask(__name__)


# db_connect = pymongo.MongoClient("mongodb://localhost:27017")  # connect to the database
#db_connect = pymongo.MongoClient(os.getenv('MONGODB_URI', 'mongodb://127.0.0.1:27017/database'))
db_connect = pymongo.MongoClient("mongodb+srv://pravinsinh27:shivay27@cluster0.lksygvr.mongodb.net/?retryWrites=true&w=majority")  # connect to the database
db = db_connect["test_db"]  # get database
collection = db["col1"]  # get collections(table )


@app.route("/read")
def read():  # function used to read user data from the mongoDB !!!!
    username = request.args.get('username')
    x = collection.find({"username": username})
    print(type(x))
    for i in x:
        i["_id"] = str(i["_id"])
    if username:
        l1= list(x)
        return username
    app.logger.info('Info level log')
    return "user is non"


if __name__ == "__main__":
    app.run(debug=True, port=5455)
