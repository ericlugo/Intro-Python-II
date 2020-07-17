class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return (f"""You are currently in the {self.name}\n{self.description}""")

    def to_n(self):
        return self.n_to

    def to_s(self):
        return self.s_to

    def to_e(self):
        return self.e_to

    def to_w(self):
        return self.w_to

    def check_items(self):
        item_names = []
        for item in self.items:
            item_names.append(" ".join(item.name.split("_")).capitalize())
        if len(item_names) > 0:
            print('> As you search around the room you see the following items.')
            for item in item_names:
                print(f'> - {item}')
        else:
            print('> There are no items in this room.')

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
                return retrieved_item
        return None

    def give_item(self, new_item):
        if new_item is not None:
            self.items.append(new_item)
        else:
            return '> I cannot drop that which I do not have...'
