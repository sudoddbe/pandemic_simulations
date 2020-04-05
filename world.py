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

    def update_infections(self):
        for p1 in self.population:
            for p2 in self.population:
                if p1 == p2:
                    continue
                else:
                    p1.spread_infection(p2)

    def setup_live_view(self):
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        liveview_healthy, = plt.plot([], [], 'bo')
        liveview_sick, = plt.plot([], [], 'ro')
        self.liveview_healthy = liveview_healthy
        self.liveview_sick = liveview_sick
        self.liveview_fig = fig
        self.liveview_ax = ax

    def update_live_view(self):
        positions = np.array([p.get_position() for p in self.population if p.infection is None])
        if positions.size != 0:
            self.liveview_healthy.set_data(positions[:,0], positions[:,1])
        else:
            self.liveview_healthy.set_data([], [])
        positions = np.array([p.get_position() for p in self.population if not p.infection is None])
        if positions.size != 0:
            self.liveview_sick.set_data(positions[:,0], positions[:,1])
        else:
            self.liveview_sick.set_data([], [])
        self.liveview_fig.canvas.draw()
        self.liveview_fig.canvas.flush_events()

    def teardown_live_view(self):
        plt.close(self.liveview_fig)
        plt.ioff()
        del self.liveview_fig
        del self.liveview_ax
        del self.liveview_healthy
        del self.liveview_sick

    def plot_world(self):
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        positions = np.array([p.get_position() for p in self.population])
        plt.plot(positions[:,0], positions[:,1], 'bo')

