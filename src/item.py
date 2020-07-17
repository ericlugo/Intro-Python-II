class Item:
    def __init__(self, name, description):
        self.name = "_".join(name.lower().split())
        self.description = description

    def __str__(self):
        return (f"""You are currently staring at a {self.name}\n{self.description}""")

    def on_take(self):
        print(
            f"""You have picked up {' '.join(self.name.split('_')).capitalize()}""")

    def on_drop(self):
        print(
            f"""You have dropped {' '.join(self.name.split("_")).capitalize()}""")
