# Ingredient class to represent an ingredient with name, amount, and unit of measure
class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name}"
class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []

    # etc.. etc..
    # Succes!
