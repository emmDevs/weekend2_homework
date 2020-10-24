import unittest
from classes.guest import Guest 
from classes.song import Song
from classes.room import Room
from classes.venue import Venue

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.example_guest_1 = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.example_guest_2 = Guest("Cyndi Lauper", 50, 60, "Girls just wanna have fun")
        self.example_guest_3 = Guest("Bob Dylan", 20, 35, "Blowin in the wind")
        self.example_guest_4 = Guest("Tom Jones", 26, 80, "It's not unusual")
        self.example_guest_5 = Guest("Dizzee Rascal", 31, 200, "Bonkers")
        self.example_guest_6 = Guest("Beyonce", 19, 40, "If I were a boy")
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

    def test_guest_can_pay_entry_fee(self):
        entry_fee = 5
        self.example_guest_1.pay_entry_fee(entry_fee)
        self.assertEqual(45, self.example_guest_1.wallet)
