# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item, Lightsource


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = [
            Item('knife', "Your trusty knife. It is fairly sharp.")]
        self.lights = 0

    def travel(self, dir):
        if getattr(self.room, f"{dir[0]}_to"):
            self.room = getattr(self.room, f"{dir[0]}_to")
        else:
            print('There is nothing is that direction')

    def inventory(self):
        print(f"{self.name}'s items:")
        for item in self.items:
            print(f"  {item.name} - {item.desc}")

    def item_action(self, cmd):
        if len(cmd) < 3 and cmd[0][0] == 'c':
            print(
                f'Improper usage. Correct usage is "{cmd[0]} [item1] [item2]"')
        elif len(cmd) < 2:
            print(
                f'Improper usage. Correct usage is "{cmd[0]} [item1]"')
        elif cmd[0][0] == 'g':
            self.get(cmd[1])
        elif cmd[0][0] == 'd':
            self.drop(cmd[1])
        elif cmd[0][0] == 'u':
            self.use(cmd[1])
        elif cmd[0][0] == 'c':
            self.craft(cmd[1], cmd[2])

    def get(self, item_name):
        item_loc = self.room.get(item_name, self.lights)
        if item_loc is not None:
            self.room.items[item_loc].get(self)
            self.items.append(self.room.items[item_loc])
            self.room.items.pop(item_loc)

    def drop(self, item_name):
        loc = None
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                loc = i
        if loc is None:
            print(f"{self.name} doesn't have a {item_name}!")
        elif isinstance(self.items[loc], Lightsource) and self.room.darkness:
            print(f'This is not a good place to do that.')
        else:
            self.items[loc].drop(self)
            self.room.items.append(self.items[loc])
            self.items.pop(loc)

    def use(self, item_name):
        print(f'Using the {item_name}...')

    def craft(self, item1_name, item2_name):
        print('Crafting...')
