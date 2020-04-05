from disease import Disease

#One instance of a disease e.g in ONE person
class Infection():
    def __init__(self, disease):
        self.disease = disease
        self.days = 0
        self.showing_symptoms = self.disease.get_showing_symptoms()
        self.contagious_radius = self.disease.get_contagious_radius(self.showing_symptoms)
        self.contagiousness = self.disease.get_contagiousness(self.showing_symptoms)
        self.recovery_chance = self.disease.get_base_recovery_chance()
