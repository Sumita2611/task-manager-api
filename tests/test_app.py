import unittest
from app import app

class TaskApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()