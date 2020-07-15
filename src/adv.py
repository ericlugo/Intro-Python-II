from room import Room
from player import Player
import time


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


# Main Loop
player = Player(room['outside'])

user_input = ['']
while not user_input[0].lower() in ['q', 'quit', 'exit']:

    # Location Callout and Entry Prompt
    time.sleep(0.5)
    print(f"""\n==========\n{player.get_location()}\n==========\n""")
    time.sleep(0.2)
    user_input = input('> ').split()
    if len(user_input) == 0:
        user_input = ['']
    time.sleep(0.5)

    # Player Movement
    if user_input[0].lower() in ['move', 'go', 'n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
        if(user_input[0].lower() in ['n', 'north']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['n', 'north']))):
            new_location = player.get_location().to_n()
            error = player.set_location(new_location)
            if error:
                print(error)
        elif (user_input[0].lower() in ['s', 'south']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['s', 'south']))):
            new_location = player.get_location().to_s()
            error = player.set_location(new_location)
            if error:
                print(error)
        elif (user_input[0].lower() in ['e', 'east']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['e', 'east']))):
            new_location = player.get_location().to_e()
            error = player.set_location(new_location)
            if error:
                print(error)
        elif (user_input[0].lower() in ['w', 'west']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['w', 'west']))):
            new_location = player.get_location().to_w()
            error = player.set_location(new_location)
            if error:
                print(error)
        else:
            print('> Please enter a valid command to proceed')

    # Exit Condition
    elif user_input[0].lower() in ['q', 'quit', 'exit']:
        print('> Now exiting the program. Thank you for your time.')

    # Invalid Command
    else:
        print('> Please enter a valid command to proceed.')
        user_input = ['']
