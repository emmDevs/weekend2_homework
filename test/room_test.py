import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.guest_2 = Guest("Cyndi Lauper", 50, 60, "Girls just wanna have fun")
        self.guest_3 = Guest("Bob Dylan", 20, 35, "Blowin in the wind")
        self.song = Song("Saturday Night Fever", "The Bee Gees", 3.22)
        self.example_room_1 = Room("stars in your eyes", 5, self.guest, self.song, [])
        self.example_room_2 = Room("Britains Got Talent", 4, self.guest, self.song, ["John Travolta", "Cyndi Lauper"])

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
