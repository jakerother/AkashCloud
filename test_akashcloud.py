# test_akashcloud.py
"""
Tests for AkashCloud module.
"""

import unittest
from akashcloud import AkashCloud

class TestAkashCloud(unittest.TestCase):
    """Test cases for AkashCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AkashCloud()
        self.assertIsInstance(instance, AkashCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AkashCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
