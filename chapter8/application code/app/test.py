import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
import unittest
import app
import json
from http import HTTPStatus

class TestAPIMethods(unittest.TestCase):
    def setUp(self):

        self.db_uri = 'sqlite:///' + os.path.join(basedir, 'test.db')
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        app.app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        self.app = app.app.test_client()
        app.db.create_all()

        cmd = "DROP TABLE IF EXISTS users"
        result = app.db.engine.execute(cmd)
        cmd = """
            CREATE TABLE users 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, identity_number INTEGER)"""
        result = app.db.engine.execute(cmd)
        cmd = "insert into users (name, surname, identity_number) VALUES ('John', 'Connor', 200509)"
        app.db.engine.execute(cmd)

    def test_get(self):
        result = app.get_user_details(1)
        expected = json.dumps({"name": "John", "surname": "Connor", "identity_number": 200509, "links":
                            [{"rel": "self", "resource": "http://127.0.0.1:8000/v1/users/1", "method": "GET"},
                             {"rel": "update", "resource": "http://127.0.0.1:8000/v1/users/1", "method": "PATCH"},
                             {"rel": "update", "resource": "http://127.0.0.1:8000/v1/users/1", "method": "DELETE"}
                             ]}), HTTPStatus.OK
        self.assertEqual(result, expected)

    def test_post(self):
        result = app.create({"name": "Peter", "surname": "Watson", "identity_number": 511247})
        result = app.get_user_details(result.lastrowid);
        expected = json.dumps({"name": "Peter", "surname": "Watson", "identity_number": 511247,
                               "links": [{"rel": "self", "resource": "http://127.0.0.1:8000/v1/users/2", "method": "GET"},
                               {"rel": "update", "resource": "http://127.0.0.1:8000/v1/users/2", "method": "PATCH"},
                               {"rel": "update", "resource": "http://127.0.0.1:8000/v1/users/2", "method": "DELETE"}]}), HTTPStatus.OK
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()