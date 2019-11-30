from flask import render_template, redirect, url_for, request, jsonify
from application import app, db
from application.forms import PostForm
from application.models import Posts
from application.snake import *


@app.route("/")
def home():
    return render_template("home.html", title="THING")


@app.route("/snakeGet", methods=["POST"])
def snakeGet():
    if runGame[0] == 1:
        return "finished"
    else:
        return jsonify(getGrid())

@app.route("/snakePut", methods=["POST"])
def snakePut():
    if request.data == b"0": #up
        change(0)
    if request.data == b"1": #down
        change(1)
    if request.data == b"2": #left
        change(2)
    if request.data == b"3": #right
        change(3)
    if request.data == b"start":
        runGame[0] = 0
        snakeStart()
    return request.data

@app.route("/snake", methods=["GET"])
def snake():
    return render_template( "snake.html", grid = [arenaX, arenaY], snakeHead = snakeHeadSymbol, snakeTail = snakeTailSymbol, fruit = fruitSymbol )


@app.route("/post", methods=["GET", "POST"])
def login():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                title = form.title.data,
                content = form.content.data
                )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        print(form.errors)
        return render_template("post.html", title="Form:", form=form)

@app.route("/register")
def register():
    return render_template("register.html", title="Register:")
