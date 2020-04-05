
class Disease():
    def __init__(self, base_recovery_chance=0.05, showing_symptoms=0.1, contagiousness=0.1, contagious_radius=0.1):
        self.base_recovery_chance = base_recovery_chance
        self.showing_symptoms = showing_symptoms
        self.contagiousness = contagiousness
        self.contagious_radius = contagious_radius

    def get_base_recovery_chance(self):
        return self.base_recovery_chance

    def get_showing_symptoms(self):
        return self.showing_symptoms

    def get_contagiousness(self, showing_symptoms):
        return self.contagiousness

    def get_contagious_radius(self, showing_symptoms):
        return self.contagious_radius

