import unittest
  
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db, bcrypt
from application.models import Player, Account_details, Scores


class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+str(getenv("MYSQL_USER"))+":"+str(getenv("MYSQL_PASSWORD"))+"@"+str(getenv("MYSQL_HOST"))+"/"+str(getenv("MYSQL_DB_TEST")))
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class Test_app(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        target_url = url_for("snake")
        redirect_url = url_for("login")
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_data_in_database(self):
        hashed_pw = bcrypt.generate_password_hash( "test" )

        player = Player(name="testName")
        db.session.add(player)

        player_id = Player.query.filter_by( name="testName" ).first().player_id

        account = Account_details( player_id=player_id, login="testName", password=hashed_pw )

        db.session.add(account)
        db.session.commit()


        player_name = Player.query.filter_by( name="testName").first().name
        self.assertEqual( player_name, "testName" )
