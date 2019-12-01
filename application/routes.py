from flask import render_template, redirect, url_for, request, jsonify, session
from application import app, db
from application.forms import PostForm
from application.models import Posts
from application.snake import Snake

sessionID = 0
gameSessions = {}


@app.route("/")
def home():
    return render_template("home.html", title="THING")


@app.route("/snakeGet", methods=["POST"])
def snakeGet():
    if gameSessions[session["ID"]].runGame[0] == 1:
        return "finished"
    else:
        return jsonify( gameSessions[session["ID"]].getGrid() )

@app.route("/snakePut", methods=["POST"])
def snakePut():
    if request.data == b"0": #up
        gameSessions[session["ID"]].change(0)
    if request.data == b"1": #down
        gameSessions[session["ID"]].change(1)
    if request.data == b"2": #left
        gameSessions[session["ID"]].change(2)
    if request.data == b"3": #right
        gameSessions[session["ID"]].change(3)
    if request.data == b"start":
        gameSessions[session["ID"]].runGame[0] = 0
        gameSessions[session["ID"]].snakeStart()
    return request.data

@app.route("/snake", methods=["GET"])
def snake():
    global sessionID
    global gameSessions
    session["ID"] = str(sessionID)
    gameSessions[str(sessionID)] = Snake()
    sessionID = sessionID + 1
    #return gameSessions[session["ID"]].test()
    return render_template( "snake.html", grid = [gameSessions[session["ID"]].arenaX, gameSessions[session["ID"]].arenaY], 
            snakeHead = gameSessions[session["ID"]].snakeHeadSymbol, snakeTail = gameSessions[session["ID"]].snakeTailSymbol, 
            fruit = gameSessions[session["ID"]].fruitSymbol )


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
