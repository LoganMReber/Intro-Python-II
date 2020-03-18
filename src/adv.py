import os
from room import Room
from player import Player
from item import Item, Lightsource
from textwrap import wrap


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Lightsource('torch', 'A torch to light the darkness')]),

    'foyer': Room("Foyer",
                  """Dim light filters in from the south. Dusty
passages run north and east.""",
                  [Item(
                      'sword',
                      'A nasty looking blade. It will stop most attackers.')],
                  True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

helpstr = ''' is not a valid command. Valid commands are:
(n)orth - Go north
(e)ast - Go east
(s)outh - Go south
(w)est - Go west
(i)tems - See held items
(g)et [item] - Pick up 'item'
(d)rop [item] - Drop 'item'
(q)uit - Quit Game

'''

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
cls()
print('\n\n============================================')
print('Welcome to Adventure Game!')
print('============================================\n')
name = input('Enter your name:')

player = Player(name, room['outside'])

# COMMAND LISTS
dir_cmds = set(('n', 'e', 's', 'w', 'north', 'east', 'south', 'west'))
item_cmds = set(('g', 'd', 'u', 'c', 'get', 'drop', 'use', 'craft'))
quit_cmds = set(('q', 'quit'))
cmd = ['']
while True:
    cls()
    print('============================================')
    if cmd[0] in dir_cmds:
        player.travel(cmd[0])
    elif cmd[0] == 'i' or cmd[0] == 'items':
        player.inventory()
    elif cmd[0] in item_cmds:
        player.item_action(cmd)
    elif cmd[0] in quit_cmds:
        break
    elif cmd[0] == '':
        pass
    else:
        print(f'\n"{cmd[0]}"{helpstr}')
    player.room.read(player.lights)
    cmd = input('==>:').split(' ')
