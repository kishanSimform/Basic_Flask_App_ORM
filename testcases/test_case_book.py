import unittest
import json

from app import main_app

class CreateBookAPITest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_book(self):
        data = {'title': 'testBook', 'author_id_': '2', 'category_id_': '3'}
        response = self.app.post('/book/', data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_book(self):
        response = self.app.get('/book/')
        self.assertEqual(response.status_code, 200)


class GetBookAPITest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_get_book(self):
        response = self.app.get('/book/all/')
        self.assertEqual(response.status_code, 200)