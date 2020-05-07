from player import Player
from room import Room

import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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
player = Player('Adventurer', room['outside'])

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


def print_room_info(room: Room) -> None:
    print(f'\nCurrent room: [{room.name}]')
    wrapper = textwrap.TextWrapper()
    desc = wrapper.fill(text=room.description)
    print(desc)


def skip_input() -> None:
    print("I don't understand that. Type [h] for valid commands.\n")


def print_help_text() -> None:
    help_text = """
Valid commands:
    [n]: move north
    [s]: move south
    [e]: move east
    [w]: move west
    [q] or [quit]: quit
    [h] or [help]: help text
    """
    print(help_text)


def move_player() -> None:
    pass


done = False

direction_dict = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to',
}

while not done:
    print_room_info(player.current_room)
    command = input('What would you like to do next?: ')

    # Check that the command is properly formatted
    if len(command) > 2 or len(command) < 1:
        skip_input()
        continue

    if command in ('n', 's', 'e', 'w'):
        player.current_room = player.move_to(command, player.current_room)
        continue

    if command in ('q', 'quit'):
        done = True
        print('\nThanks for playing! Hope to see you again soon!')
        continue

    if command in ('h', 'help'):
        print_help_text()
        continue

    else:
        skip_input()
        continue
