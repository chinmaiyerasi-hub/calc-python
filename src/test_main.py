import unittest
from app import app  # import your Flask app

class FoodBlogTestCase(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Check that the home page loads successfully
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        # Check that the page contains expected text
        response = self.app.get("/")
        html = response.data.decode("utf-8")

        self.assertIn("🍽️ My Food Blog", html)
        self.assertIn("Margherita Pizza", html)
        self.assertIn("Chocolate Cake", html)
        self.assertIn("Pasta Alfredo", html)

    def test_home_html_structure(self):
        # Ensure basic HTML tags are present
        response = self.app.get("/")
        html = response.data.decode("utf-8")

        self.assertIn("<h1>", html)
        self.assertIn("<ul>", html)
        self.assertIn("</ul>", html)

if __name__ == "__main__":
    unittest.main()
