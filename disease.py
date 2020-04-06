
class Disease():
    def __init__(self, base_recovery_chance=0.05, showing_symptoms_chance=0.2, contagiousness=0.1, contagious_radius=0.05):
        self.base_recovery_chance = base_recovery_chance
        self.showing_symptoms_chance = showing_symptoms_chance
        self.contagiousness = contagiousness
        self.contagious_radius = contagious_radius

    def get_recovery_chance(self, days):
        if days < 5:
            return 0
        return self.base_recovery_chance

    def get_showing_symptoms_chance(self):
        return self.showing_symptoms_chance

    def get_contagiousness(self, showing_symptoms):
        return self.contagiousness

    def get_contagious_radius(self, showing_symptoms):
        return self.contagious_radius

