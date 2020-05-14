from room import Room
from player import Player

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
player = Player(room['outside'])

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
user_input = ['']
while not user_input[0].lower() in ['q', 'quit']:
    print(player.get_location())
    user_input = input('> ').split()

    if user_input[0].lower() in ['move', 'go', 'n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
        if (user_input[0].lower() in ['n', 'north']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['n', 'north']))):
            new_location = player.get_location().to_n()
            move_response = player.set_location(new_location)
            print(move_response)
        elif (user_input[0].lower() in ['s', 'south']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['s', 'south']))):
            new_location = player.get_location().to_s()
            move_response = player.set_location(new_location)
            print(move_response)
        elif (user_input[0].lower() in ['e', 'east']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['e', 'east']))):
            new_location = player.get_location().to_e()
            move_response = player.set_location(new_location)
            print(move_response)
        elif (user_input[0].lower() in ['w', 'west']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['w', 'west']))):
            new_location = player.get_location().to_w()
            move_response = player.set_location(new_location)
            print(move_response)
        else:
            print('Please enter a valid command to proceed')
    elif (user_input[0].lower() in ['q', 'quit']):
        print('Now exiting the program. Thank you for your time.')
    else:
        print('Please enter a valid command in order to proceed.')
