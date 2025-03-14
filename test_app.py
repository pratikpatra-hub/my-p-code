# test_app.py
import unittest
from app import greet

class TestGreetFunction(unittest.TestCase):
    
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

if __name__ == "__main__":
    unittest.main()

