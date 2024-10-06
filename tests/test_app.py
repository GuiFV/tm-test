import unittest
from flask import Flask
from app import db, create_app
from models import Policy


class TestApp(unittest.TestCase):
    """Tests for flask API application"""
    def setUp(self):
        """Creates artifacts and instances for tests"""
        self.app_instance = create_app()
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            # pass
            db.create_all()
            item = Policy(name='test_item_policy')
            db.session.add(item)
            db.session.commit()

        self.data1 = {'id': 1, 'name': 'test_item_policy'}

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


    def test_runs(self):
        """Verifies if test suite runs successfully"""
        self.assertEqual(True, True)

    def test_app_exists(self):
        """Verifies if flask application exists"""
        self.assertEqual(type(self.app_instance), type(Flask(__name__)))

    def test_home_works(self):
        """Verifies if root endpoint works"""
        endpoint = '/'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_inexistent_endpoint(self):
        """Verifies if random endpoint returns nothing but 404 error"""
        endpoint = '/some_endpoint'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 404)

    def test_return_policy(self):
        """Verifies if policy endpoint can return data"""
        response = self.client.get('/policy/1')
        self.assertEqual(response.json, self.data1)

    def test_return_policy_not_found(self):
        """verify if policy endpoint returns 404 error if policy does not exist"""
        response = self.client.get('/policy/2')
        self.assertEqual(response.status_code, 404)


