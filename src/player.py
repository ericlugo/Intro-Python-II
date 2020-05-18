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

    def check_items(self):
        item_names = []
        for item in self.items:
            item_names.append(" ".join(item.name.split("_")).capitalize())
        return item_names

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
            return '> I cannot take what is not.'
