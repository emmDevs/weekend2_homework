class Venue:

    def __init__(self, name, till, guest, room):
        self.name = name
        self.till = till
        self.guest = guest
        self.room = room

    def charge_entry_fee(self, entry_fee):
        self.till += entry_fee
