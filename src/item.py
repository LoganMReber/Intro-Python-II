class Item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self):
        print(f"You've picked up the {self.name}")
        print(self.desc)

    def on_drop(self):
        print(f"You've dropped the {self.name}")
