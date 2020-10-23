import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.example_song_1 = Song("Saturday Night Fever", "The Bee Gees", 3.22)

    def test_song_has_a_title(self):
        self.assertEqual("Saturday Night Fever", self.example_song_1.title) 

    def test_song_has_an_artist(self):
        self.assertEqual("The Bee Gees", self.example_song_1.artist)  