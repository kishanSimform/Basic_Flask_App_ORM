import unittest
import json

from app import main_app

class LoginAPITest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_login_user(self):
        data = {'email_id': 'kishan@gmail.com', 'password': 'kishan1234'}
        response = self.app.post('/login/', data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)


class CreateUserAPITest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_user(self):
        data = {'first_name': 'test', 'email_id': 'test@gmail.com', 'password': 'test123'}
        response = self.app.post('/users/', data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)

