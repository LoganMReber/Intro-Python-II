from room import Room
from player import Player
from textwrap import wrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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

# Make a new player object that is currently in the 'outside' room.
name = input('Enter your name:')
player = Player(name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
command = ['']
while command[0] != 'q' and command[0] != 'quit':
    if command[0] == 'n' or command[0] == 'north':
        if player.room.n_to:
            player.room = player.room.n_to
        else:
            print('There is nothing is that direction')
    elif command[0] == 'e' or command[0] == 'east':
        if player.room.e_to:
            player.room = player.room.e_to
        else:
            print('There is nothing is that direction')
    elif command[0] == 's' or command[0] == 'south':
        if player.room.s_to:
            player.room = player.room.s_to
        else:
            print('There is nothing is that direction')
    elif command[0] == 'w' or command[0] == 'west':
        if player.room.w_to:
            player.room = player.room.w_to
        else:
            print('There is nothing is that direction')
    elif command[0] == 'i' or command[0] == 'items':
        print('Items:')
        for item in player.items:
            print(f'{item.name} - {item.desc}')
    elif command[0] == 'g' or command[0] == 'get':
        if len(command) > 1:
            player.get(command[1])
        else:
            print('Incorrect usage. Correct usage is "get [item name]"')
    elif command[0] == 'd' or command[0] == 'drop':
        if len(command) > 1:
            player.drop(command[1])
        else:
            print('Incorrect usage. Correct usage is "drop [item name]"')
    elif command[0] == 'q' or command[0] == 'quit' or command[0] == '':
        pass
    else:
        print(f'''\n"{command[0]}" is not a valid command. Valid commands are:
(n)orth - Go north
(e)ast - Go east
(s)outh - Go south
(w)est - Go west
(i)tems - See held items
(g)et [item] - Pick up 'item'
(d)rop [item] - Drop 'item'
(q)uit - Quit Game\n''')
    print()
    print(player.room.name)
    desc = wrap(player.room.desc)
    for line in desc:
        print(line)
    if len(player.room.items):
        print('You can see these items:')
        for i in range(len(player.room.items)):
            print(player.room.items[i].name)
    print()
    command = input('Enter a command:').split(' ')
