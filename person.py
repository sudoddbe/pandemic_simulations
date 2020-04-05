
class Person():
    def __init__(self, world, position = None, targets = None, infection = None):
        self.world = world
        self.position = position if not position is None else self.world.get_random_position()
        self.targets = targets if not targets is None else self.position
        self.infection = infection
        self.recovered = False

    def get_position(self):
        return self.position
