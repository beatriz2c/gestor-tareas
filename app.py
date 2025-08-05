from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    tareas_var = list(collection.find())
    return render_template("index.html", tareas=tareas_var)

@app.route("/add_task", methods=["POST"])
def add_task():
    descripcion = request.form["descripcion"]
    if descripcion:
        nueva_tarea = {
            "Descripcion": descripcion
        }
        collection.insert_one(nueva_tarea)
    return redirect("/")

@app.route("/delete_task/<task_id>", methods=["POST"])
def delete_task(task_id):
    collection.delete_one({"_id": ObjectId(task_id)})
    return redirect("/")

@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        nueva_descripcion = request.form["descripcion"]
        if nueva_descripcion:
            collection.update_one(
                {"_id": ObjectId(task_id)},
                {"$set": {"Descripcion": nueva_descripcion}}
            )
        return redirect("/")
    else:
        tarea = collection.find_one({"_id": ObjectId(task_id)})
        return render_template("edit_task.html", tarea=tarea)

app.run(debug=True)