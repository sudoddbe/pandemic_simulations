import numpy as np
import matplotlib.pyplot as plt
from disease import Disease
from infection import Infection
from world import World
from person import Person

if __name__=="__main__":
    world = World()
    disease = Disease()
    persons = [Person(world = world, target = world.get_new_target()) for i in range(100)]
    persons[0].infection = Infection(disease=disease)
    world.setup_live_view()
    world.update_history()
    plt.show()
    for time in range(200):
        world.update_live_view()
        world.update_all_positions()
        world.update_infections()
        world.update_recoveries()
        world.update_history()
        plt.pause(0.01)
    world.teardown_live_view()
