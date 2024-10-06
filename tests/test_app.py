import unittest
from flask import Flask
from app import app


class TestApp(unittest.TestCase):
    """Tests for flask API application"""
    def setUp(self):
        """Creates artifacts and instances for tests"""
        self.app_instance = app

        with app.test_client() as client:
            self.app = client

    def test_runs(self):
        """Verifies if test suite runs successfully"""
        self.assertEqual(True, True)

    def test_app_exists(self):
        """Verifies if flask application exists"""
        self.assertEqual(type(self.app_instance), type(Flask(__name__)))

    def test_home_works(self):
        """Verifies if root endpoint works"""
        endpoint = '/'
        response = self.app.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_inexistent_endpoint(self):
        """Verifies if random endpoint returns nothing but 404 error"""
        endpoint = '/some_endpoint'
        response = self.app.get(endpoint)
        self.assertEqual(response.status_code, 404)
        