class Stap:
    def __init__(self, beschrijving):
        self.stap = []
        self.beschrijving = beschrijving

    def voeg_stap_toe(self, stap):
        self.stap.append(stap)

    def get_stappen(self):
        return self.stap