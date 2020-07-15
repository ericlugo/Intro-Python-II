class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def get_location(self):
        return self.current_room

    def set_location(self, room):
        if room is None:
            return '> You are unable to proceed in that direction.'
        else:
            self.current_room = room
