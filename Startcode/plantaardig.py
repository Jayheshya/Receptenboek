class PlantaardigAlternatief:
    def __init__(self, naam, kcal=None):
        self.naam = naam
        self.kcal = kcal

    def __str__(self):
        if self.kcal is not None:
            return f"{self.naam} [{self.kcal} kcal]"
        return self.naam
