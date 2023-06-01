import unittest
import json

from app import main_app

class CreateCategoryAPITest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = main_app.test_client()
        self.app.testing = True
        return super().setUp() 
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_category(self):
        data = {'name': 'testCategory'}
        response = self.app.post('/category/', data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_category(self):
        response = self.app.get('/category/')
        self.assertEqual(response.status_code, 200)
