import unittest
from classes.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.example_guest_1 = Guest("John Travolta", 34, 50, "Saturday Night Fever")

    def test_guest_has_name(self):
        self.assertEqual("John Travolta", self.example_guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(34, self.example_guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.example_guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Saturday Night Fever", self.example_guest_1.favourite_song)