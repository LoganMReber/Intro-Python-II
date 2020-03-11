# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = [
            Item('knife', "Your trusty knife. It's fairly sharp")]

    def get(self, item_name):
        getting = None
        for i in range(len(self.room.items)):
            if self.room.items[i].name == item_name:
                getting = i
                self.room.items[i].on_take()
                break
        if isinstance(getting, int):
            self.items.append(self.room.items[getting])
            self.room.items.pop(getting)
        else:
            print(f'What? There is no {item_name} here!')

    def drop(self, item_name):
        dropping = None
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                dropping = i
                self.items[i].on_drop()
                break
        if isinstance(dropping, int):
            self.room.items.append(self.items[dropping])
            self.items.pop(dropping)
        else:
            print(f"What? You don't have a {item_name}!")
