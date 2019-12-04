from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(player_id):
    return Account_details.query.get(int(player_id))


class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    account_details = db.relationship("Account_details", backref="player", lazy=True)
    scores = db.relationship("Scores", backref="player", lazy=True)

    def __repr__(self):
        return "".join([
                "Name: ", self.name
            ])


class Account_details(db.Model, UserMixin):
    login_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"))
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    id = login_id

    def __repf__(self):
        return "".join([
                "login: ", self.login
            ])
            

class Scores(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"))
    score = db.Column(db.Integer, nullable=False)

    def __repf__(self):
        return "".join([
                "score: ", self.score
            ])

