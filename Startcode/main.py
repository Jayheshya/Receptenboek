
from recept import Recept, Ingredient
from stap import Stap

def main():


    recepten = []

    # Maak een nieuw recept aan
    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")

    # Voeg ingrediënten toe
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram"))

    # Voeg stappen toe aan het recept
    recept1.voeg_stap_toe(Stap("Snijd de kip in blokjes."))
    recept1.voeg_stap_toe(Stap("Kook de sperziebonen."))
    recept1.voeg_stap_toe(Stap("Bak de kip en voeg de sperziebonen toe."))


    recepten.append(recept1)

    # Maak een nieuw recept aan
    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")

    # Voeg ingrediënten toe
    recept2.voeg_ingredient_toe(Ingredient("gehakt", 300, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 2, "stuks"))

    # Voeg stappen toe aan het recept
    recept2.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden."))
    recept2.voeg_stap_toe(Stap("Bak het gehakt rul in een pan."))
    recept2.voeg_stap_toe(Stap("Snijd de paprika in stukjes en voeg toe aan het gehakt."))
    recept2.voeg_stap_toe(Stap("Doe het mengsel in een quichevorm en bak 25 minuten.")) 

    recepten.append(recept2)

    # Print automatisch alle recepten
    for recept in recepten:
        print(f"\nIngrediënten voor {recept._Recept__naam}:")
        for ingredient in recept.get_ingredienten():
            print(f"- {ingredient}")
        print("Stappen:")
        for stap in recept.get_stappen():
            print(f"- {stap.beschrijving}")

    # enzovoort...
    # Veel succes!

if __name__ == "__main__":
    main()
