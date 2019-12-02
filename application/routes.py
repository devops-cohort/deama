from flask import render_template, redirect, url_for, request, jsonify, session
from application import app, db, bcrypt, login_manager
from application.forms import PostForm, RegistrationForm, LoginForm
from application.models import Posts, Account_details, Scores, Player
from application.snake import Snake
from flask_login import login_user, current_user, logout_user, login_required

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


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))




@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("snake"))

    form = LoginForm()
    if form.validate_on_submit():
        user = Account_details.query.filter_by( login=form.login.data ).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("snake"))

    return render_template("login.html", title="Login:", form=form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash( form.password.data )

        player = Player(name=form.login.data)
        db.session.add(player)

        player_id = Player.query.filter_by( name=form.login.data ).first().player_id

        account = Account_details( player_id = player_id, login=form.login.data, password=hashed_pw )

        db.session.add(account)
        db.session.commit()
        return redirect( url_for("snake") )
    return render_template("register.html", title="", form=form)
