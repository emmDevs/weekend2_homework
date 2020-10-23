import unittest
from classes.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.example_guest_1 = Guest("John Travolta", 34, 50, "Saturday Night Fever")

    def test_guest_has_name(self):
        self.assertEqual("John Travolta", self.example_guest_1.name)