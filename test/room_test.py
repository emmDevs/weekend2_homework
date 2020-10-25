import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.venue import Venue

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.guest_2 = Guest("Cyndi Lauper", 50, 60, "Girls just wanna have fun")
        self.guest_3 = Guest("Bob Dylan", 20, 35, "Blowin in the wind")
        self.guest_4 = Guest("Tom Jones", 26, 80, "It's not unusual")
        self.guest_5 = Guest("Dizzee Rascal", 31, 200, "Bonkers")
        self.guest_6 = Guest("Beyonce", 19, 40, "If I were a boy")
        self.song = Song("Saturday Night Fever", "The Bee Gees", 3.22)
        self.song_2 = Song("Girls just wanna have fun", "Cyndi Lauper", 2.58)
        self.song_3 = Song("Blowin in the wind", "Bob Dylan", 4.15)
        self.song_4 = Song("It's not unusual", "Tom Jones", 3.42)
        self.song_5 = Song("Bonkers", "Dizzee Rascal", 3.12)
        self.song_6 = Song("If I were a boy", "Beyonce", 4.11)
        self.example_room_1 = Room("stars in your eyes", 5, self.guest, self.song, [], [])
        self.example_room_2 = Room("Britains Got Talent", 4, self.guest, self.song, ["John Travolta", "Cyndi Lauper"], [])
        self.example_room_3 = Room("The Voice", 4, self.guest, self.song, ["John Travolta", "Cyndi Lauper", "Dizzee Rascal", "Beyonce"], [{
            "title": "Saturday Night Fever",
            "Artist": "The Bee Gees",
            "length": 3.22,
        },
        {
            "title": "Girls just wanna have fun",
            "Artist": "Cyndi Lauper",
            "length": 2.58,
        },
        {
            "title": "Blowin in the wind",
            "Artist": "Bob Dylan",
            "length": 4.15
        }
        ])

    def test_room_has_name(self):
        self.assertEqual("stars in your eyes", self.example_room_1.name)

    def test_room_has_a_capacity(self):
        self.assertEqual(5, self.example_room_1.capacity)

    def test_room_has_a_guest(self):
        self.assertEqual("John Travolta", self.example_room_1.guest.name)

    def test_room_has_a_song(self):
        self.assertEqual("Saturday Night Fever", self.example_room_1.song.title)

    def test_room_has_a_checked_in_list(self):
        self.assertEqual(0, len(self.example_room_1.checked_in_list))

    def test_guest_can_check_into_room(self):
        self.example_room_1.check_guest_into_room(self.guest)
        self.assertEqual(1, len(self.example_room_1.checked_in_list))

    def test_guest_can_check_out_of_room(self):
        self.example_room_2.check_guest_out_of_room(self.guest)
        self.assertEqual(1, len(self.example_room_2.checked_in_list))

    def test_guest_can_check_out_of_room__name_not_in_list(self):
        self.example_room_2.check_guest_out_of_room(self.guest_3)
        self.assertEqual(2, len(self.example_room_2.checked_in_list))

    def test_room_has_a_playlist(self):
        self.assertEqual(0, len(self.example_room_1.playlist))

    def test_can_add_song_to_room(self):
        self.example_room_1.add_song_to_room(self.song)
        self.assertEqual(1, len(self.example_room_1.playlist))

    def test_guest_can_check_into_room__too_many_people(self):
        self.example_room_3.check_guest_into_room(self.guest_4)
        self.assertEqual("Sorry, maximum occupancy reached", self.example_room_3.check_guest_into_room(self.guest_4))

    def test_room_has_playlist__room_3_added_playlist(self):
        self.assertEqual(3, len(self.example_room_3.playlist))

    def test_if_favourite_song_on_playlist__yes(self):
        self.example_room_3.check_song_on_playlist(self.guest)
        self.assertEqual("Yay! They have my favourite song!", self.example_room_3.check_song_on_playlist(self.guest))

