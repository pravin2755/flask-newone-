import pymongo
from flask import Flask, request, render_template
app = Flask(__name__)
# db_connect = pymongo.MongoClient("mongodb://localhost:27017")  # connect to the database
db_connect = pymongo.MongoClient(
    "mongodb+srv://pravinsinh27:shivay27@cluster0.lksygvr.mongodb.net/?retryWrites=true&w=majority")  # connect to the database
db = db_connect["test_db"]  # get database
collection = db["col1"]  # get collections(table )
@app.route("/add_data", methods=["GET", "POST"])
def create():  # used to create user and  store data to the mongoDB!!!
    if request.method == "POST":
        username = request.form["username"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        dict1 = {"username": username, "first_name": first_name, "last_name": last_name, "email": email,
                 "password1": password1, "password2": password2}
        # db.products.insertMany( [
        # { item: "card", qty: 15 },
        # { item: "envelope", qty: 20 },                                #it is used for insert many data !!!!
        # { item: "stamps" , qty: 30 }
        # ] );
        collection.insert_one(dict1)

    return render_template("demo.html")
