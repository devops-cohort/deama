import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db, bcrypt
from application.models import Account_details, Scores


class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+str(getenv("MYSQL_USER"))+":"+str(getenv("MYSQL_PASSWORD"))+"@"+str(getenv("MYSQL_HOST"))+"/"+str(getenv("MYSQL_DB_TEST")))
        return app

    def setUp(self):
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

        account = Account_details( login="testName", password=hashed_pw )

        db.session.add(account)
        db.session.commit()


        player_name = Account_details.query.filter_by( login="testName").first().login
        self.assertEqual( player_name, "testName" )

        hashed_pw = bcrypt.generate_password_hash( "test" )
        player_password = Account_details.query.filter_by( login=player_name ).first().password
        self.assertEqual( bcrypt.check_password_hash(player_password, "test"), True )
        
