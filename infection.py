from disease import Disease
import numpy as np

#One instance of a disease e.g in ONE person
class Infection():
    def __init__(self, disease):
        self.disease = disease
        self.days = 0
        self.showing_symptoms_chance = self.disease.get_showing_symptoms_chance()
        self.showing_symptoms = False
        self.contagious_radius = self.disease.get_contagious_radius(self.showing_symptoms)
        self.contagiousness = self.disease.get_contagiousness(self.showing_symptoms)
        self.recovery_chance = self.disease.get_recovery_chance(self.days)

    def update_infection(self):
        self.days += 1
        symptom_days = 5.0
        if self.days < symptom_days and not self.showing_symptoms:
            self.showing_symptoms = np.random.uniform() < 1 - (1 - self.showing_symptoms_chance)**(1/symptom_days)

        self.contagious_radius = self.disease.get_contagious_radius(self.showing_symptoms)
        self.contagiousness = self.disease.get_contagiousness(self.showing_symptoms)
        self.recovery_chance = self.disease.get_recovery_chance(self.days)
