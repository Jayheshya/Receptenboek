from stap import Stap

class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten_lijst = []
        self.__stappen = []

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten_lijst.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredienten_lijst

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def get_stappen(self):
        return self.__stappen

# Ingredient class 
class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid

    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam}"
    
