from disease import Disease

#One instance of a disease e.g in ONE person
class Infection():
    def __init__(self, disease):
        self.disease = disease
        self.days = 0
        self.showing_symptoms = self.disease.get_showing_symptoms()
        self.contagious = self.disease.get_contagious(self.showing_symptoms)
        self.recovery_chance = self.get_recovery_chance()
