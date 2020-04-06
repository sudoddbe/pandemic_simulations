import numpy as np
from infection import Infection

class Person():
    def __init__(self, world, position = None, target = None, infection = None):
        self.world = world
        self.position = position if not position is None else self.world.get_random_position()
        self.target = target
        self.infection = infection
        self.recovered = False
        world.population.append(self)

    def get_position(self):
        return self.position

    def update_position(self, speed = 0.01):
        if self.target is None:
            self.position += speed*np.random.randn(*self.position.shape)
        else:
            direction = self.target - self.position
            norm = np.linalg.norm(direction)
            if norm < speed:
                self.position = self.target
                self.target = self.world.get_new_target()
            else:
                direction /= norm
                self.position += direction*speed

        self.position = self.world.clamp_position(self.position)

    def update_infection(self):
        if self.infection is None:
            return
        self.infection.update_infection()
        if np.random.uniform() < self.infection.recovery_chance:
            self.infection = None
            self.recovered = True

    def spread_infection(self, other):
        if self.infection is None or other.recovered or (not other.infection is None):
            return

        if np.linalg.norm(self.position - other.position) < self.infection.contagious_radius:
            if np.random.uniform() < self.infection.contagiousness:
                other.infection = Infection(disease = self.infection.disease)
