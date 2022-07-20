import csv

from flask_migrate import Migrate
import pandas as pd
import psycopg2
import pymongo
import requests
from flask import render_template, Flask, request, jsonify, make_response, Response, send_file
from flask_pymongo import PyMongo
from datetime import datetime
import flask
from flask_sqlalchemy import SQLAlchemy

# app = flask.Flask(__name__)

app = Flask(__name__)


# app.config["MONGO_URI"] = "mongodb://localhost:27017"
# mongo = PyMongo(app)
# app.config["MONGO_URI"] = False
# mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
# db = mongodb_client.db
#
# @app.route("/add_one")
# def add_one():
#     db.todos.insert_one({'title': "todo title", 'body': "todo body"})
#     return flask.jsonify(message="success")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
# mongodb_client = PyMongo(app)
# db = mongodb_client.db

@app.route("/", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        print('working')
        username = request.form["username"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password1 = request.form["password1"]

        password2 = request.form["password2"]
        db_connect = pymongo.MongoClient("mongodb://localhost:27017")  # connect to the database
        db = db_connect["test_db"]  # database get
        collection = db["col1"]  # collections(table )get
        all_database = db_connect.list_databases_names
        print(all_database)
        dict1 = {"username": username, "first_name": first_name, "last_name": last_name, "email": email,
                 "password1": password1, "password2": password2}
        collection.insert_one(dict1)

    return render_template("demo.html")


@app.route("/update")
# @app.route("/")  # both url are valid.
def update():
    # usename = username
    usename = request.args.get('username')
    db_connect = pymongo.MongoClient("mongodb://localhost:27017")
    db = db_connect["test_db"]  # database get
    collection = db["col1"]  # collections(table )get
    # a = db.col1.find({'username': usename})
    myquery = {'username': usename}
    newvalues = {"$set": {"email": " cjrfrfygvb@gmail.com"}}
    collection.update_one(myquery, newvalues)
    return render_template("demo.html")


@app.route("/del")
def delete():
    usename = request.args.get('username')
    db_connect = pymongo.MongoClient("mongodb://localhost:27017")
    db = db_connect["test_db"]
    collection = db["col1"]
    collection.delete_one({'username': usename})
    return render_template("demo.html")


@app.route("/read")
def read():
    usename = request.args.get('username')
    db_connect = pymongo.MongoClient("mongodb://localhost:27017")
    db = db_connect["test_db"]
    collection = db["col1"]
    x = collection.find_one({"username": usename})
    x["_id"] = str(x["_id"])
    return x

    # for x in collection.find({"username":usename}):
    #     print(x)
    # return render_template("demo.html")


@app.route("/download")
def down():
    usename = request.args.get('username')
    db_connect = pymongo.MongoClient("mongodb://localhost:27017")
    db = db_connect["test_db"]
    collection = db["col1"]
    # x = collection.find()
    # print(type(x),x)
    x = collection.find_one({'username':usename})
    df = pd.DataFrame([x])
    df.to_csv("friend.csv")
    path = r'C:\Users\pravinsinh.gohil\Desktop\pravin flask\friend.csv'
    return send_file(path, as_attachment=True)




if __name__ == "__main__":
    app.run(debug=True, port=5000)
