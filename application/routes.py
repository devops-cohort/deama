from flask import render_template, redirect, url_for, request, jsonify, session
from application import app, db, bcrypt
from application.forms import PostForm, RegistrationForm
from application.models import Posts, Account_details, Scores, Player
from application.snake import Snake

sessionID = 0
gameSessions = {}
color = "grey"


@app.route("/")
def home():
    return render_template("home.html", title="Snake game online")



@app.route("/snakeGetScore", methods=["POST"])
def snakeGetScore():
    return jsonify( gameSessions[session["ID"]].getScore() )

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
            fruit = gameSessions[session["ID"]].fruitSymbol, color = color )


@app.route("/login", methods=["GET", "POST"])
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

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash( form.password.data )
        print( bcrypt.check_password_hash(hashed_pw, "thing") )

        player = Player(name=form.login.data)
        db.session.add(player)

        player_id = Player.query.filter_by( name=form.login.data ).first().player_id

        account = Account_details( player_id = player_id, login=form.login.data, password=hashed_pw )

        db.session.add(account)
        db.session.commit()
        return redirect( url_for("snake") )
    return render_template("register.html", title="", form=form)
