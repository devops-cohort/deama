import unittest
  
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Player, Account_details, Scores


class TestBase(TestCase):

    def create_app(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


class Test_app(TestCase):

    def test_homepage_view(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
