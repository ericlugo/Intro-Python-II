from item import Item
from room import Room
from player import Player
import time

# Declare all items
item = {
    'key': Item("Rusty Key", "Looks so old you're pretty sure this will break on use."),
    'mirror': Item("Faded Mirror",
                   "This mirror is so faded that your reflection looks like someone else..."),
    'hard candy': Item("Hard Candy", "Huh? Where did I get this from..?"),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['mirror']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['key']]),
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
player = Player(room['outside'], [item['hard candy']])

user_input = ['']
while not user_input[0].lower() in ['q', 'quit', 'exit']:

    # INTERFACE PAUSE AND INPUT RETRIEVAL
    time.sleep(0.5)
    print(
        f"""\n================================================\n{player.get_location()}\n================================================\n""")
    time.sleep(0.2)
    user_input = input('> ').split()
    if len(user_input) == 0:
        user_input = ['']
    time.sleep(0.5)

    # PLAYER MOVEMENT
    if user_input[0].lower() in ['move', 'go', 'n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
        if (user_input[0].lower() in ['n', 'north']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['n', 'north']))):
            new_location = player.get_location().to_n()
            error = str(player.set_location(new_location))
            if error:
                print(error)
        elif (user_input[0].lower() in ['s', 'south']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['s', 'south']))):
            new_location = player.get_location().to_s()
            error = str(player.set_location(new_location))
            if error:
                print(error)
        elif (user_input[0].lower() in ['e', 'east']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['e', 'east']))):
            new_location = player.get_location().to_e()
            error = str(player.set_location(new_location))
            if error:
                print(error)
        elif (user_input[0].lower() in ['w', 'west']) or (len(user_input) > 1 and ((user_input[0].lower() in ['move', 'go']) and (user_input[1].lower() in ['w', 'west']))):
            new_location = player.get_location().to_w()
            error = str(player.set_location(new_location))
            if error:
                print(error)
        else:
            print('> Please enter a valid command to proceed')

    # ITEM SEARCH
    elif (user_input[0].lower() in ['look', 'search']) or (len(user_input) > 1 and ((user_input[0].lower() in ['check', 'search']) and (user_input[1].lower() in ['room', 'items']))):
        room_items = player.get_location().check_items()
        if len(room_items) > 0:
            print('> As you search around the room you see the following items')
            for item in room_items:
                print(f'> - {item}')
        else:
            print('> There are no items in this room')

    # ITEM RETRIEVAL
    elif user_input[0].lower() in ['get', 'take']:
        if len(user_input) > 1:
            item = player.get_location().get_item(" ".join(user_input[1:]))
            if item is None:
                print(f'> Unable to locate {" ".join(user_input[1:])}')
            else:
                player.give_item(item)
        else:
            print('> You must specify which item you which to interact with')

    # ITEM DROP
    elif user_input[0].lower() in ['drop', 'leave']:
        if len(user_input) > 1:
            item = player.get_item(" ".join(user_input[1:]))
            if item is None:
                print(f'> Unable to drop {" ".join(user_input[1:])}')
            else:
                player.get_location().give_item(item)
        else:
            print('> You must specify which item you which to interact with')

    # INVENTORY CHECK
    elif (user_input[0].lower() in ['i', 'items', 'inventory', 'bag']) or (len(user_input) > 1 and ((user_input[0].lower() in ['check', 'search']) and (user_input[1].lower() in ['items', 'inventory', 'bag']))):
        player_items = player.check_items()
        if len(player_items) > 0:
            print('> Your inventory currently holds the following items')
            for item in player_items:
                print(f'> - {item}')
        else:
            print('> There are no items in your bag')

    # GAME EXIT
    elif user_input[0].lower() in ['q', 'quit', 'exit']:
        print('> Now exiting the program. Thank you for your time.')

    # INVALID COMMAND
    else:
        print('> Please enter a valid command to proceed.')
        user_input = ['']
