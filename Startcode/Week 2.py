from recept import Recept
from ingredient import Ingredient
from stap import Stap
from hoeveelheden import pas_hoeveelheden_aan

def main():


    recepten = []

    # Maak een nieuw recept aan
    recept1 = Recept("Kwetiau Ayam", "Gewokte rijstnoedels met kip en chinese kool.")

    # Voeg ingrediënten toe (voorbeeld kcal-waardes)
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram", plantaardig_alternatief="tofu", kcal=550))
    recept1.voeg_ingredient_toe(Ingredient("chinese kool", 400, "gram", kcal=40))
    recept1.voeg_ingredient_toe(Ingredient("kwetiau rijstnoedels", 250, "gram", kcal=900))

    # Voeg stappen toe aan het recept
    recept1.voeg_stap_toe(Stap("Snijd de kip in reepjes."))
    recept1.voeg_stap_toe(Stap("Snijd de chinese kool in reepjes."))
    recept1.voeg_stap_toe(Stap("Kook de kwetiau rijstnoedels volgens de aanwijzingen op de verpakking."))
    recept1.voeg_stap_toe(Stap("Bak de kip in een grote wokpan totdat deze gaar is."))
    recept1.voeg_stap_toe(Stap("Voeg de chinese kool toe en roerbak totdat deze zacht is."))
    recept1.voeg_stap_toe(Stap("Voeg de gekookte kwetiau rijstnoedels toe en meng alles goed door elkaar."))

    recepten.append(recept1)

    # Maak een nieuw recept aan
    recept2 = Recept("Rendang", "Traditioneel West-Sumatraans rundvlees gerecht.")

    # Voeg ingrediënten toe
    recept2.voeg_ingredient_toe(Ingredient("rendang boemboe", 1, "stuk", kcal=100))
    recept2.voeg_ingredient_toe(Ingredient("sucadelappen", 1, "kilo", plantaardig_alternatief="jackfruit", kcal=1800))
    recept2.voeg_ingredient_toe(Ingredient("kokosmelk", 400, "ml", kcal=800))
    recept2.voeg_ingredient_toe(Ingredient("water", 200, "ml", kcal=0))
    recept2.voeg_ingredient_toe(Ingredient("laos", 2, "cm", kcal=5))
    recept2.voeg_ingredient_toe(Ingredient("sereh", 2, "stengels", kcal=5))
    recept2.voeg_ingredient_toe(Ingredient("kaneel", 1, "stokje", kcal=5))
    recept2.voeg_ingredient_toe(Ingredient("gula djawa", 2, "el", kcal=80))
    recept2.voeg_ingredient_toe(Ingredient("zout", 1, "tl", kcal=0))    
    recept2.voeg_ingredient_toe(Ingredient("rijst", 300, "gram", kcal=1050))

    # Voeg stappen toe aan het recept
    recept2.voeg_stap_toe(Stap("Snijd het vlees in blokjes van 2 cm."))
    recept2.voeg_stap_toe(Stap("Verhit een beetje olie in een grote pan en bak het vlees rondom bruin."))
    recept2.voeg_stap_toe(Stap("Voeg de rendang boemboe toe en bak dit kort mee."))
    recept2.voeg_stap_toe(Stap("Voeg de kokosmelk, water, laos, sereh, kaneel, gula djawa en zout toe."))
    recept2.voeg_stap_toe(Stap("Breng het geheel aan de kook en laat het op laag vuur sudderen totdat het vlees gaar is en de saus is ingedikt (ongeveer 3-4 uur)."))
    recept2.voeg_stap_toe(Stap("Kook ondertussen de rijst volgens de aanwijzingen op de verpakking."))
    recept2.voeg_stap_toe(Stap("Serveer de rendang met de gekookte rijst."))

    recepten.append(recept2)

    # Zelfde voor recept3
    recept3 = Recept("Babi Pangang", "Noord-Sumatraanse buikspek.") 
    recept3.voeg_ingredient_toe(Ingredient("hamlappen", 500, "gram", plantaardig_alternatief="tempeh", kcal=1200))
    recept3.voeg_ingredient_toe(Ingredient("knoflook", 1, "teen", kcal=5))
    recept3.voeg_ingredient_toe(Ingredient("ui", 1, "stuk", kcal=30))
    recept3.voeg_ingredient_toe(Ingredient("oestersaus", 2, "eetlepels", kcal=40))
    recept3.voeg_ingredient_toe(Ingredient("ketjap manis", 2, "eetlepels", kcal=60))
    recept3.voeg_ingredient_toe(Ingredient("sambal oelek", 1, "theelepel", kcal=5))
    recept3.voeg_ingredient_toe(Ingredient("gember", 1, "cm", kcal=2))
    recept3.voeg_ingredient_toe(Ingredient("palm suiker", 1, "theelepel", kcal=20))
    recept3.voeg_ingredient_toe(Ingredient("maizena", 1, "eetlepel", kcal=35))

    recept3.voeg_stap_toe(Stap("Snij de hamlappen in dunne repen en marineer het met de rest van ingrediënten voor de marinade."))
    recept3.voeg_stap_toe(Stap("Laat het vlees nu minimaal 1 uur of langer marineren."))
    recept3.voeg_stap_toe(Stap("Bak het vlees in een klein beetje olie in een ruime koekenpan totdat het goudbruin is."))
    recept3.voeg_stap_toe(Stap("Maak tegelijkertijd de saus door het uitje fijn te snipperen."))
    recept3.voeg_stap_toe(Stap("Verhit een beetje olie in een steelpan met dikke bodem en fruit het uitje aan tot deze zacht en glazig is."))
    recept3.voeg_stap_toe(Stap("Knijp dan de knoflookteentjes uit en voeg deze toe. Bak even kort mee."))
    recept3.voeg_stap_toe(Stap("Maak een papje van de maizena met een beetje water en voeg dit toe aan het uitje en knoflook."))
    recept3.voeg_stap_toe(Stap("Serveer de saus over de stukjes gebakken varkensvlees eventueel met een beetje atjar tjampoer, rijst en komkommer erbij."))
                                       
    recepten.append(recept3)

    recept4 = Recept("Sajoer Lodeh", "Groentencurry in kokosmelk.")
    recept4.voeg_ingredient_toe(Ingredient("wortel", 2, "stukken", kcal=60))
    recept4.voeg_ingredient_toe(Ingredient("sperziebonen", 200, "gram", kcal=60))
    recept4.voeg_ingredient_toe(Ingredient("kousenband", 100, "gram", kcal=30))
    recept4.voeg_ingredient_toe(Ingredient("aubergine", 1, "stuk", kcal=25))
    recept4.voeg_ingredient_toe(Ingredient("courgette", 1, "stuk", kcal=20))
    recept4.voeg_ingredient_toe(Ingredient("kokosmelk", 400, "ml", kcal=800))
    recept4.voeg_ingredient_toe(Ingredient("sajoer lodeh boemboe", 1, "zakje", kcal=100))

    recepten.append(recept4)

    # Vraag het aantal personen
    try:
        aantal_personen = int(input("Voor hoeveel personen wil je het recept maken? "))
    except ValueError:
        aantal_personen = 4

    # Print automatisch alle recepten met aangepaste hoeveelheden en kcal
    for recept in recepten:
        print(f"\nIngrediënten voor {recept._Recept__naam} (voor {aantal_personen} personen):")
        aangepaste_ingredienten = pas_hoeveelheden_aan(recept.get_ingredienten(), aantal_personen)
        totale_kcal = 0
        factor = aantal_personen / 4
        for i, ingredient in enumerate(recept.get_ingredienten()):
            # Bereken kcal per ingrediënt
            try:
                kcal = float(ingredient.kcal) * factor
            except ValueError:
                kcal = 0
            totale_kcal += kcal
            print(f"- {aangepaste_ingredienten[i]}")
        print("Stappen:")
        for stap in recept.get_stappen():
            print(f"- {stap.beschrijving}")
        print(f"Totale kcal per persoon: {int(totale_kcal // aantal_personen)} kcal")

    # enzovoort...
    # Veel succes!

if __name__ == "__main__":
    main()
