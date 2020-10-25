class Venue:

    def __init__(self, name, till, guest, room, bar_tab):
        self.name = name
        self.till = till
        self.guest = guest
        self.room = room
        self.bar_tab = bar_tab

    def charge_entry_fee(self, entry_fee):
        self.till += entry_fee

    def add_item_to_bar_tab(self, bar_tab):
        self.bar_tab.append(bar_tab)

    def get_total_bill_for_room(self, room):
        total_bill = 0
        for item in self.bar_tab:
            if item["room"] == room.name:
                total_bill += item["amount"]
        return total_bill

    def get_total_bill_for_customer(self, guest):
        total_bill = 0
        for item in self.bar_tab:
            if item["guest"] == guest.name:
                total_bill += item["amount"]
        return total_bill

