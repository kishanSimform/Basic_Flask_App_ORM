import unittest
import json

from app import main_app

class CreateAuthorAPITest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_author(self):
        data = {'name': 'testAuthor', 'email_id': 'testauthor@gmail.com', 'address': 'India', 'gender': 'F'}
        response = self.app.post('/author/', data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_auhtor(self):
        response = self.app.get('/author/')
        self.assertEqual(response.status_code, 200)
