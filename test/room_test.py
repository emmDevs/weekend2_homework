import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

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

