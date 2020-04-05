import numpy as np
import matplotlib.pyplot as plt
from disease import Disease
from infection import Infection
from world import World
from person import Person

if __name__=="__main__":
    world = World()
    disease = Disease()
    persons = [Person(world = world), Person(world = world)]
    plt.figure()
    world.plot_world(persons)
    plt.show()
