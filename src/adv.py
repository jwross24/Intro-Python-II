from item import Item
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     items=[
                         Item(
                             'torch',
                             "It's glowing a faint yellow."
                         )
                     ]),

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


def skip_input() -> None:
    print(
        "I don't understand that command. Type [h] for a list of commands.\n")


def print_help_text() -> None:
    help_text = """
Valid commands:
    [n]: move north
    [s]: move south
    [e]: move east
    [w]: move west
    [i] or [inventory]: view inventory
    [get]/[take] [item]: take item from room
    [drop] [item]: drop item in room
    [q] or [quit]: quit
    [h] or [help]: help text
    """
    print(help_text)


done = False

print('\nWelcome to your new adventure!')
print('==============================\n')
print('Type [h] for commands.\n')

while not done:
    player.current_room.print_room_info()
    player_input = input('\nWhat would you like to do? \n> ').split()
    command = player_input[0]

    if command in ('n', 's', 'e', 'w'):
        player.current_room = player.move_to(command)
        continue

    if command in ('q', 'quit'):
        done = True
        print('\nThanks for playing!')
        continue

    if command in ('h', 'help'):
        print_help_text()
        continue

    if command in ('i', 'inventory'):
        player.print_inventory()
        continue

    if command in ('get', 'take'):
        item_name = ' '.join(player_input[1:])  # multi-word item support
        player.inventory = player.take_item(item_name)
        player.current_room.items = player.current_room.take_item(item_name)
        continue

    if command == 'drop':
        item_name = ' '.join(player_input[1:])  # multi-word item support
        player.inventory = player.drop_item(item_name)
        continue

    else:
        skip_input()
        continue
