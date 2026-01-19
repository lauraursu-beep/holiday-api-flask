from app import app
import unittest

class HolidayAPITestCase(unittest.TestCase):
    def test_get_holiday(self):
        self.app = app.test_client()
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_holiday(self):
        self.app = app.test_client()
        response = self.app.post('/holiday', json={
            'holidayName': 'Easter',
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
