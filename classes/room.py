class Room:

    def __init__(self, name, capacity, guest, song, checked_in_list):
        self.name = name
        self.capacity = capacity
        self.guest = guest
        self.song = song
        self.checked_in_list = checked_in_list

    def check_guest_into_room(self, guest):
        self.checked_in_list.append(guest.name)