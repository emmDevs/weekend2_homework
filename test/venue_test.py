import unittest
from classes.venue import Venue 
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar_tab import Bar_tab

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
        self.bar_tab = Bar_tab(self.example_room_3.name, 5, "entry fee", self.guest_6.name)
        self.example_venue = Venue("Codeclan Caraoke", 500, self.guest, self.example_room_1,[{
            "room": "stars in your eyes",
            "amount": 5,
            "description": "entry fee",
            "guest": "John Travolta"
        },
        {
            "room": "stars in your eyes",
            "amount": 7.50,
            "description": "White Wine",
            "guest": "John Travolta" 
        }
        ])
        

    def test_venue_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.example_venue.name)

    def test_venue_has_till(self):
        self.assertEqual(500, self.example_venue.till)

    def test_venue_has_guest(self):
        self.assertEqual("John Travolta", self.example_venue.guest.name)

    def test_venue_has_a_room(self):
        self.assertEqual("stars in your eyes", self.example_venue.room.name)

    def test_take_money_from_guest(self):
        entry_fee = 5
        self.example_venue.charge_entry_fee(entry_fee)
        self.assertEqual(505, self.example_venue.till)

    def test_venue_has_a_bar_tab(self):
        self.assertEqual(2, len(self.example_venue.bar_tab))

    def test_venue_can_add_item_to_bar_tab(self):
        self.example_venue.add_item_to_bar_tab(self.bar_tab)
        self.assertEqual(3, len(self.example_venue.bar_tab))

    def test_venue_can_add_total_bill_for_room(self):
        self.example_venue.get_total_bill_for_room(self.example_room_1)
        self.assertEqual(12.50, self.example_venue.get_total_bill_for_room(self.example_room_1))