

# Ingredient class 

class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, plantaardig_alternatief=None):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid
        self.plantaardig_alternatief = plantaardig_alternatief

    def __str__(self):
        basis = f"{self.hoeveelheid} {self.eenheid} {self.naam}"
        if self.plantaardig_alternatief:
            basis += f" (plantaardig alternatief: {self.plantaardig_alternatief})"
        return basis
    
