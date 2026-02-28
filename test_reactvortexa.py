# test_reactvortexa.py
"""
Tests for ReactVortexa module.
"""

import unittest
from reactvortexa import ReactVortexa

class TestReactVortexa(unittest.TestCase):
    """Test cases for ReactVortexa class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReactVortexa()
        self.assertIsInstance(instance, ReactVortexa)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReactVortexa()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
