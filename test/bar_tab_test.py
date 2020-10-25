import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.venue import Venue

class TestBar_tab(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Travolta", 34, 50, "Saturday Night Fever")
        self.bar_tab = Bar_tab(5, "entry_fee", self.guest)