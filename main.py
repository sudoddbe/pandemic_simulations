import numpy as np
import matplotlib.pyplot as plt
from disease import Disease
from infection import Infection
from world import World
from person import Person

if __name__=="__main__":
    world = World()
    disease = Disease()
    persons = [Person(world = world, target = np.array([0.5, 0.5])) for i in range(10)]
    world.setup_live_view()
    plt.show()
    for time in range(20):
        world.update_live_view()
        world.update_all_positions()
        plt.pause(0.1)
    world.teardown_live_view()
