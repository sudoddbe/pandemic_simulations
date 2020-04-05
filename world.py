import numpy as np
import matplotlib.pyplot as plt

class World():
    def __init__(self, bounding_box = (0,0,1.0,1.0)):
        self.bb=np.array(bounding_box)

    def get_random_position(self):
        return np.random.uniform(low = self.bb[0:2], high=self.bb[2:4])

    def plot_world(self, persons=[]):
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        positions = np.array([p.get_position() for p in persons])
        plt.plot(positions[:,0], positions[:,1], 'bo')

