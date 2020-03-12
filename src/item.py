class Item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def item_action(self, player, cmd):
        if cmd == 't':
            on_take()
        elif cmd == 'd':
            on_drop()

    def get(self, player):
        print(f"{player.name} picked up the {self.name}")
        print(f'{self.name} - {self.desc}')

    def drop(self, player):
        print(f"{player.name} dropped the {self.name}")


class Lightsource(Item):
    def get(self, player):
        player.lights += 1
        super().get(player)

    def drop(self, player):
        player.lights -= 1
        if not player.lights:
            print('You no longer have a source of light!')
        super().drop(player)
