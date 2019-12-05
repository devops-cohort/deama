from sqlalchemy import desc
from flask import render_template, redirect, url_for, request, jsonify, session
from application import app, db, bcrypt, login_manager
from application.forms import RegistrationForm, LoginForm, AccountUpdateForm
from application.models import Account_details, Scores
from application.snake import Snake
from flask_login import login_user, current_user, logout_user, login_required

db.create_all()

gameSessions = {}
snakeBackgroundColor = "grey"


@app.route("/")
def home():
    return render_template("home.html", title="Snake game online")





@app.route("/account", methods=["GET","POST"])
def account():
    if current_user.is_authenticated:
        form = AccountUpdateForm()
        if form.validate_on_submit():
            if form.delete.data:
                player_name = Account_details.query.filter_by( player_id=current_user.get_id() ).first()
                db.session.delete(player_name)

                player_scores = Scores.query.filter_by( player_id=None )
                for deleted in player_scores:
                    db.session.delete(deleted)

                db.session.commit()
                return redirect(url_for("login"))

            else:
                current_user.login = form.new_login.data

                player_name = Account_details.query.filter_by( player_id=current_user.get_id() ).first()
                player_name.name = form.new_login.data

                db.session.commit()
                return redirect(url_for("account"))
        elif request.method == "GET":
            form.new_login.data = current_user.login

        return render_template("account.html", title = "Account update", form = form)

    return redirect(url_for("login"))


@app.route("/snakeFinish", methods=["POST"])
def snakeFinish():
    if current_user.is_authenticated:
        scoreNumber = Scores.query.filter_by( player_id=current_user.get_id() ). \
            filter_by( score=gameSessions[session["ID"]].getScore() ).first()

        if scoreNumber == None:
            score = Scores( player_id=current_user.get_id(), score=gameSessions[session["ID"]].getScore() )
            db.session.add(score)
            db.session.commit()

        return "done"
    return "not authenticated"


@app.route("/snakeGetScore", methods=["POST"])
def snakeGetScore():
    return jsonify( gameSessions[session["ID"]].getScore() )

@app.route("/snakeGet", methods=["POST"])
def snakeGet():
    if gameSessions[session["ID"]].gameState == "finished":
        return "finished"
    else:
        return jsonify( gameSessions[session["ID"]].getGrid() )

@app.route("/snakePut", methods=["POST"])
def snakePut():
    if request.data == b"0": #up
        gameSessions[session["ID"]].changeDirection(0)
    if request.data == b"1": #down
        gameSessions[session["ID"]].changeDirection(1)
    if request.data == b"2": #left
        gameSessions[session["ID"]].changeDirection(2)
    if request.data == b"3": #right
        gameSessions[session["ID"]].changeDirection(3)
    if request.data == b"start":
        gameSessions[session["ID"]].snakeStop()
        gameSessions[session["ID"]].gameState = ""
        gameSessions[session["ID"]].snakeStart()
    return request.data

@app.route("/snake", methods=["GET"])
def snake():
    if current_user.is_authenticated:

        global gameSessions
        session["ID"] = str(current_user.get_id())
        gameSessions[str(current_user.get_id())] = Snake()
        return render_template( "snake.html", grid = [gameSessions[session["ID"]].arenaX, gameSessions[session["ID"]].arenaY], 
                snakeHead = gameSessions[session["ID"]].snakeHeadSymbol, snakeTail = gameSessions[session["ID"]].snakeTailSymbol, 
                fruit = gameSessions[session["ID"]].fruitSymbol, color = snakeBackgroundColor )

    return redirect(url_for("login"))


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

    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("snake"))

    form = RegistrationForm()
    if form.validate_on_submit():
            hashed_pw = bcrypt.generate_password_hash( form.password.data )

            account = Account_details( login=form.login.data, password=hashed_pw )

            db.session.add(account)
            db.session.commit()
            return redirect( url_for("snake") )
    return render_template("register.html", title="Register", form=form)


@app.route("/scores", methods=["GET","POST"])
def scores():
    if current_user.is_authenticated:
        scoreEntries = Scores.query.filter_by( player_id=current_user.get_id() )
        scoreEntries = scoreEntries.order_by(desc(Scores.score))

        allTimeHigh = Scores.query.filter_by() #query.all() doesn't seem to work with order_by()
        allTimeHigh = allTimeHigh.order_by(desc(Scores.score)).first()

        allTimeHigh_id = allTimeHigh.player_id

        allTimeHighName = Account_details.query.filter_by( player_id=allTimeHigh_id ).first().login

        return render_template("scores.html", title="Scores: ", scoreEntries = scoreEntries, allTimeHigh = allTimeHigh.score,
                allTimeHighName = allTimeHighName)

    return redirect(url_for("login"))
