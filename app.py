import sys
import random
from flask import Flask, redirect, render_template, request, session
from flask_session import Session


print(sys.version)
print(sys.executable)

app = Flask(__name__)
app.config["SESSIONS_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def tasks():
    if "todos" not in session:
        session["todos"] = []
    return render_template("etasks.html", todos=session["todos"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        session["todos"].append(todo)
        return redirect("/")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        if "todos" not in session:
            session["todos"] = []
        return render_template("delete.html", todos=session["todos"])
    else:
        todo = request.form.get("task")
        session["todos"].remove(todo)
        return redirect("/")