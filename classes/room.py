class Room:

    def __init__(self, name, capacity, guest, song, checked_in_list, playlist):
        self.name = name
        self.capacity = capacity
        self.guest = guest
        self.song = song
        self.checked_in_list = checked_in_list
        self.playlist = playlist

    def check_guest_into_room(self, guest):
        self.checked_in_list.append(guest.name)

    def check_guest_out_of_room(self, guest):
        if guest.name in self.checked_in_list:
            self.checked_in_list.remove(guest.name)