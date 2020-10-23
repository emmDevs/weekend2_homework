import unittest
from classes.guest import Guest 
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.example_guest_1 = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.example_song_1 = Song("Saturday Night Fever", "The Bee Gees", 3.22)
        self.example_room_1 = Room("stars in your eyes", 5, self.example_guest_1, self.example_song_1, [], [])

    def test_guest_has_name(self):
        self.assertEqual("John Travolta", self.example_guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(34, self.example_guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.example_guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Saturday Night Fever", self.example_guest_1.favourite_song)

    # def test_guest_can_check_into_room(self):
    # #     result = guest list length will be 1
    #     self.assertEqual(1, len(self.example_room_1.guest_list))