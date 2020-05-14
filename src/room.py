# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

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
