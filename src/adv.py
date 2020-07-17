from item import Item
from room import Room
from player import Player
import time


# Declare all expected commands
# - Expected Basic Command List:
basic_movement = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']
basic_inventory = ['i', 'items', 'inventory', 'b', 'bag']
basic_search = ['find', 'look', 'search']
exit_commands = ['q', 'quit', 'exit']
# - Expected Verbose Command List:
movement_verbs = ['move', 'go']
movement_directions = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']
inventory_verbs = ['check', 'open']
inventory_objects = ['inventory', 'bag']
search_verbs = ['search']
search_objects = ['room', 'items']
pickup_verbs = ['get', 'take', 'pickup']  # Followed by "item name"
drop_verbs = ['drop', 'leave']  # Followed by "item name"
inspection_verbs = ['inspect']  # Followed by "item name"


# Declare all of the items
item = {
    'pez dispenser': Item("Pez Dispenser", "Never leave home without it!"),
    'rusty sword': Item("Rusty Sword", "Looks like it might break if you swing it..."),
    'moldy shield': Item("Moldy Shield", "There's so much mold you can't see what it is made of!"),
}


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [item['rusty sword']]),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [item['moldy shield']]),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
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
player = Player(room['outside'], [item['pez dispenser']])

user_input = ['']
while not user_input[0].lower() in exit_commands:

    # Location Callout and Entry Prompt
    time.sleep(0.5)
    print(f"""\n==========\n{player.get_location()}\n==========\n""")
    time.sleep(0.2)
    user_input = input('> ').split()
    if len(user_input) == 0:
        user_input = ['']
    time.sleep(0.5)

    # Simple Commands:
    if len(user_input) == 1:
        if user_input[0].lower() in basic_movement:
            player.change_location(user_input[0].lower())
        elif user_input[0].lower() in basic_inventory:
            player.check_items()
        elif user_input[0].lower() in basic_search:
            player.get_location().check_items()
        elif user_input[0].lower() in exit_commands:
            print('> Now exiting the program. Thank you for your time.')
        else:
            print('> Please enter a valid command to proceed.')

    # Verbose Commands:
    elif len(user_input) > 1:
        if user_input[0].lower() in movement_verbs:
            if user_input[1].lower() in movement_directions:
                player.change_location(user_input[1].lower())
            else:
                print('> Please enter a valid command to proceed.')
        elif user_input[0].lower() in inventory_verbs:
            if user_input[1].lower() in inventory_objects:
                player.check_items()
            else:
                print('> Please enter a valid command to proceed.')
        elif user_input[0].lower() in search_verbs:
            if user_input[1].lower() in search_objects:
                player.get_location().check_items()
            else:
                print('> Please enter a valid command to proceed.')
        elif user_input[0].lower() in pickup_verbs:
            if len(user_input) > 1:
                item_name = " ".join(user_input[1:])
                item = player.get_location().get_item(item_name)
                if item is None:
                    print(f'> Unable to locate {item_name}.')
                else:
                    player.give_item(item)
            else:
                print('> You must specify which item you which to interact with.')
        elif user_input[0].lower() in drop_verbs:
            if len(user_input) > 1:
                item_name = " ".join(user_input[1:])
                item = player.get_item(item_name)
                if item is None:
                    print(f'> Unable to drop {item_name}')
                else:
                    player.get_location().give_item(item)
            else:
                print('> You must specify which item you which to interact with.')
        elif user_input[0].lower() in inspection_verbs:
            if len(user_input) > 1:
                item_name = " ".join(user_input[1:])
                retrieved_item = player.check_for_item(item_name)
                if retrieved_item is None:
                    retrieved_item = player.get_location().check_for_item(item_name)
                if retrieved_item is None:
                    print(f'> Unable to inspect {item_name}.')
                else:
                    print(retrieved_item)
            else:
                print('> You must specify which item you which to interact with.')
        else:
            print('> Please enter a valid command to proceed.')
            user_input = ['']
