import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.song = Song("Saturday Night Fever", "The Bee Gees", 3.22)
        self.example_room_1 = Room("stars in your eyes", 5, Guest, Song)

    def test_room_has_name(self):
        self.assertEqual("stars in your eyes", self.example_room_1.name)

    def test_room_has_a_capacity(self):
        self.assertEqual(5, self.example_room_1.capacity)