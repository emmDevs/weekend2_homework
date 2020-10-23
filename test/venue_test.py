import unittest
from classes.venue import Venue 
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.guest_2 = Guest("Cyndi Lauper", 50, 60, "Girls just wanna have fun")
        self.guest_3 = Guest("Bob Dylan", 20, 35, "Blowin in the wind")
        self.guest_4 = Guest("Tom Jones", 26, 80, "It's not unusual")
        self.guest_5 = Guest("Dizzee Rascal", 31, 200, "Bonkers")
        self.guest_6 = Guest("Beyonce", 19, 40, "If I were a boy")
        self.song = Song("Saturday Night Fever", "The Bee Gees", 3.22)
        self.example_room_1 = Room("stars in your eyes", 5, self.guest, self.song, [], [])
        self.example_room_2 = Room("Britains Got Talent", 4, self.guest, self.song, ["John Travolta", "Cyndi Lauper"], [])
        self.example_room_3 = Room("The Voice", 4, self.guest, self.song, ["John Travolta", "Cyndi Lauper", "Dizzee Rascal", "Beyonce"], [])
        self.example_venue = Venue("Codeclan Caraoke", 500, self.guest, self.example_room_1)

    def test_venue_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.example_venue.name)

    def test_venue_has_till(self):
        self.assertEqual(500, self.example_venue.till)