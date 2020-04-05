import numpy as np
import matplotlib.pyplot as plt

class World():
    def __init__(self, bounding_box = (0,0,1.0,1.0), population = []):
        self.bb=np.array(bounding_box)
        self.population = population

    def get_random_position(self):
        return np.random.uniform(low = self.bb[0:2], high=self.bb[2:4])

    def get_new_target(self):
        return self.get_random_position()

    def clamp_position(self, position):
        position[0] = max(position[0], self.bb[0])
        position[0] = min(position[0], self.bb[2])
        position[1] = max(position[1], self.bb[1])
        position[1] = min(position[1], self.bb[3])
        return position

    def update_all_positions(self):
        for p in self.population:
            p.update_position()

    def setup_live_view(self):
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        liveview, = plt.plot([], [], 'bo')
        self.liveview = liveview
        self.liveview_fig = fig
        self.liveview_ax = ax

    def update_live_view(self):
        positions = np.array([p.get_position() for p in self.population])
        self.liveview.set_data(positions[:,0], positions[:,1])
        self.liveview_fig.canvas.draw()
        self.liveview_fig.canvas.flush_events()

    def teardown_live_view(self):
        plt.close(self.liveview_fig)
        plt.ioff()
        del self.liveview_fig
        del self.liveview_ax
        del self.liveview

    def plot_world(self):
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        positions = np.array([p.get_position() for p in self.population])
        plt.plot(positions[:,0], positions[:,1], 'bo')

