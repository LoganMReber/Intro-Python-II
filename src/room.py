# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room():
    def __init__(self, name, desc, items=[], darkness=False):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items
        self.darkness = darkness

    def read(self, lights):
        print('============================================\n')
        print('\n============================================')
        print(self.name)
        print('--------------------------------------------')
        if not lights and self.darkness:
            print("It's pitch black. You cant see a thing")
            print('============================================')
        else:
            print(self.desc)
            if len(self.items):
                print('--------------------------------------------')
                print('You see some items:')
            for item in self.items:
                print(f' {item.name}')
            print('============================================')

    def get(self, item_name, lights):
        if not lights and self.darkness:
            print("It's far too dark to do that!")
            return None
        loc = None
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                loc = i
        if loc is None:
            print(f"There is no {item_name} here!")
        return loc
