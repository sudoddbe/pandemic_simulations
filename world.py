import numpy as np
import matplotlib.pyplot as plt

class World():
    def __init__(self, bounding_box = (0,0,1.0,1.0), population = []):
        self.bb=np.array(bounding_box)
        self.population = population
        self.nbr_of_recovered = []
        self.nbr_of_healthy = []
        self.nbr_of_infected = []


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
            other_people = [op for op in self.population if np.linalg.norm(op.position - p.position) < p.comfort_radius]
            p.update_position(other_people=other_people)

    def update_infections(self):
        for p1 in self.population:
            for p2 in self.population:
                if p1 == p2:
                    continue
                else:
                    p1.spread_infection(p2)

    def update_recoveries(self):
        for p in self.population:
            p.update_infection()

    def update_history(self):
        self.nbr_of_infected.append(len(self.get_infected_population()))
        self.nbr_of_healthy.append(len(self.get_healthy_population()))
        self.nbr_of_recovered.append(len(self.get_recovered_population()))

    def get_healthy_population(self):
        return [p for p in self.population if p.infection is None]

    def get_recovered_population(self):
        return [p for p in self.population if p.recovered]

    def get_infected_population(self):
        return [p for p in self.population if not p.infection is None]


    def setup_live_view(self):
        plt.ion()
        fig = plt.figure()
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        liveview_healthy, = plt.plot([], [], 'bo')
        liveview_sick, = plt.plot([], [], 'ro')
        liveview_recovered, = plt.plot([], [], 'go')
        self.liveview_healthy = liveview_healthy
        self.liveview_sick = liveview_sick
        self.liveview_recovered = liveview_recovered
        self.liveview_population_fig = fig

        fig = plt.figure()
        plt.ylim([0.0, 1.0])
        self.liveview_stackpop_fig = fig

    def update_live_view(self):
        positions = np.array([p.get_position() for p in self.get_healthy_population()])
        if positions.size != 0:
            self.liveview_healthy.set_data(positions[:,0], positions[:,1])
        else:
            self.liveview_healthy.set_data([], [])

        positions = np.array([p.get_position() for p in self.get_infected_population()])
        if positions.size != 0:
            self.liveview_sick.set_data(positions[:,0], positions[:,1])
        else:
            self.liveview_sick.set_data([], [])

        positions = np.array([p.get_position() for p in self.get_recovered_population()])
        if positions.size != 0:
            self.liveview_recovered.set_data(positions[:,0], positions[:,1])
        else:
            self.liveview_recovered.set_data([], [])

        self.liveview_population_fig.canvas.draw()
        self.liveview_population_fig.canvas.flush_events()

        if len(self.nbr_of_healthy) >= 2:

            ax = self.liveview_stackpop_fig.gca()
            population_size = len(self.population)*1.0
            x = [len(self.nbr_of_healthy) - 1, len(self.nbr_of_healthy)]
            infected = np.array(self.nbr_of_infected[-2:]) / population_size
            healthy = np.array(self.nbr_of_healthy[-2:])/population_size
            recovered =  np.array(self.nbr_of_recovered[-2:]) / population_size
            healthy = healthy - recovered
            ax.stackplot(x,infected, healthy, recovered,  colors=['r', 'b', 'g'])

    def teardown_live_view(self):
        plt.close(self.liveview_stackpop_fig)
        plt.close(self.liveview_population_fig)
        plt.ioff()
        del self.liveview_population_fig
        del self.liveview_stackpop_fig
        del self.liveview_healthy
        del self.liveview_sick

    def plot_world(self):
        plt.xlim((self.bb[0], self.bb[2]))
        plt.ylim((self.bb[1], self.bb[3]))
        positions = np.array([p.get_position() for p in self.population])
        plt.plot(positions[:,0], positions[:,1], 'bo')

