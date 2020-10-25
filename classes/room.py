class Room:

    def __init__(self, name, capacity, guest, song, checked_in_list, playlist):
        self.name = name
        self.capacity = capacity
        self.guest = guest
        self.song = song
        self.checked_in_list = checked_in_list
        self.playlist = playlist

    def check_guest_into_room(self, guest):
        if len(self.checked_in_list) < self.capacity:
            self.checked_in_list.append(guest.name)
        return "Sorry, maximum occupancy reached"

    def check_guest_out_of_room(self, guest):
        if guest.name in self.checked_in_list:
            self.checked_in_list.remove(guest.name)

    def add_song_to_room(self, song):
        self.playlist.append(song.title)

    def check_song_on_playlist(self, guest):
        for item in self.playlist:
            if guest.favourite_song == item["title"]:
                return "Yay! They have my favourite song!"
            return "Boo! They don't have my favourite song."