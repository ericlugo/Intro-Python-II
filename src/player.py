# CARDINAL DIRECTIONS:
north = ['n', 'north']
south = ['s', 'south']
east = ['e', 'east']
west = ['w', 'west']


class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def get_location(self):
        return self.current_room

    def set_location(self, room):
        if room is None:
            return '> You are unable to proceed in that direction.'
        else:
            self.current_room = room

    def change_location(self, direction):
        if (direction in north):
            new_location = self.get_location().to_n()
            error = self.set_location(new_location)
            if error:
                print(error)
        elif (direction in south):
            new_location = self.get_location().to_s()
            error = self.set_location(new_location)
            if error:
                print(error)
        elif (direction in east):
            new_location = self.get_location().to_e()
            error = self.set_location(new_location)
            if error:
                print(error)
        elif (direction in west):
            new_location = self.get_location().to_w()
            error = self.set_location(new_location)
            if error:
                print(error)

    def check_items(self):
        item_names = []
        for item in self.items:
            item_names.append(" ".join(item.name.split("_")).capitalize())
        if len(item_names) > 0:
            print('> Your inventory currently holds the following items:')
            for item in item_names:
                print(f'> - {item}')
        else:
            print('> Your bag is currently empty.')

    def check_for_item(self, item_name):
        for item in self.items:
            if "_".join(item_name.split()) == item.name:
                return item
        return None

    def get_item(self, item_name):
        for index, item in enumerate(self.items):
            if "_".join(item_name.split()) == item.name:
                retrieved_item = item
                self.items.pop(index)
                retrieved_item.on_drop()
                return retrieved_item
        return None

    def give_item(self, new_item):
        if new_item is not None:
            self.items.append(new_item)
            new_item.on_take()
        else:
            return '> I cannot take that which is not available.'
