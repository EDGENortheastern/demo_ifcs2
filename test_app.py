import unittest
from app import HelloName  # Adjust the import based on the actual filename

class TestHelloName(unittest.TestCase):
    
    def setUp(self):
        # Set up the HelloName instance
        self.app = HelloName()

    def test_presence_check(self):
        self.assertTrue(self.app.presence_check("John"))
        self.assertFalse(self.app.presence_check(""))

    def test_length_check(self):
        self.assertTrue(self.app.length_check("John"))
        self.assertFalse(self.app.length_check("J"))
        self.assertFalse(self.app.length_check(""))

if __name__ == "__main__":
    unittest.main()