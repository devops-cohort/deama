from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(player_id):
    return Account_details.query.get(int(player_id))


class Account_details(db.Model, UserMixin):
    player_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    id = player_id #satisfy UserMixin requirements

    scores = db.relationship("Scores", backref="account_details", lazy=True)

    def __repf__(self):
        return "".join([
                "login: ", self.login
            ])
            

class Scores(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("account_details.player_id"))
    score = db.Column(db.Integer, nullable=False)

    def __repf__(self):
        return "".join([
                "score: ", self.score
            ])

