import numpy as np
from infection import Infection

class Person():
    def __init__(self, world, position = None, target = None, infection = None, comfort_radius = 0.02):
        self.world = world
        self.position = position if not position is None else self.world.get_random_position()
        self.target = target
        self.infection = infection
        self.recovered = False
        self.comfort_radius = comfort_radius
        world.population.append(self)

    def get_position(self):
        return self.position

    def go_along_line(self, other_people, steps, step_size, direction):
        s = 0
        while(s < steps):
            if np.linalg.norm(self.position - self.target) < step_size:
                self.position = self.target
                self.target = self.world.get_new_target()
                return None, 0
            self.position += step_size*direction
            for op in other_people:
                if op == self:
                    continue
                diff = op.position - self.position
                norm = np.linalg.norm(diff)
                if norm < self.comfort_radius:
                    return op, steps - s
            s += 1
        return None, 0
    def go_along_comfort_zone(self, other, other_people, steps_left, step_size):
        s = 0
        angular_step_size = 2*np.pi*step_size / (2*np.pi*self.comfort_radius)
        while (s < steps_left and s*angular_step_size < np.pi):
            diff = self.position - other.position
            angle = np.arctan2(diff[1], diff[0])
            change_vector = np.array([np.cos(angle + angular_step_size), np.sin(angle + angular_step_size)]) * self.comfort_radius
            self.position = other.position + change_vector
            for op in other_people:
                if op == self:
                    continue
                if op == other:
                    continue
                diff = op.position - self.position
                norm = np.linalg.norm(diff)
                if norm < self.comfort_radius:
                    return
            s += 1


    def update_position(self, speed = 0.01, other_people=[]):
        if not self.infection is None:
            speed = speed if not self.infection.showing_symptoms else speed * 0.0
        if self.target is None:
            self.position += speed*np.random.randn(*self.position.shape)
        else:
            direction = self.target - self.position
            norm = np.linalg.norm(direction)
            direction /= norm
            steps = 100
            step_size = speed / steps
            op, steps_left = self.go_along_line(other_people, steps, step_size, direction)
            if op is not None and steps_left:
                self.go_along_comfort_zone(op, other_people, steps_left, step_size)
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
