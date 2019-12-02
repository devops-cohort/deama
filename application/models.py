from application import db

######################################################################
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return "".join([
            "User: ", self.first_name, "", self.last_name, "/r/n",
            "Title: ", self.title, "/r/n", self.content
            ])
######################################################################

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "".join([
                "Name: ", self.name
            ])


class Account_details(db.Model):
    login_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.player_id"))
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

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

