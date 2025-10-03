from recept import Recept
from ingredient import Ingredient
from stap import Stap
from hoeveelheden import pas_hoeveelheden_aan
from plantaardig import PlantaardigAlternatief

def main():


    recepten = []

    # Maak een nieuw recept aan
    recept1 = Recept("Kwetiau Ayam", "Gewokte rijstnoedels met kip en chinese kool.")

    # Voeg ingrediënten toe (voorbeeld kcal-waardes)
    recept1.voeg_ingredient_toe(Ingredient("kip", 125, "gram", plantaardig_alternatief=PlantaardigAlternatief("tofu", 80), kcal=138))
    recept1.voeg_ingredient_toe(Ingredient("chinese kool", 100, "gram", kcal=10))
    recept1.voeg_ingredient_toe(Ingredient("kwetiau rijstnoedels", 62.5, "gram", kcal=225))

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
    recept2.voeg_ingredient_toe(Ingredient("rendang boemboe", 1, "stuk", kcal=25))
    recept2.voeg_ingredient_toe(Ingredient("sucadelappen", 250, "gram", plantaardig_alternatief=PlantaardigAlternatief("jackfruit", 40), kcal=450))
    recept2.voeg_ingredient_toe(Ingredient("kokosmelk", 100, "ml", kcal=200))
    recept2.voeg_ingredient_toe(Ingredient("water", 50, "ml", kcal=0))
    recept2.voeg_ingredient_toe(Ingredient("laos", 2, "cm", kcal=1))
    recept2.voeg_ingredient_toe(Ingredient("sereh", 2, "stengels", kcal=1))
    recept2.voeg_ingredient_toe(Ingredient("kaneel", 1, "stokje", kcal=1))
    recept2.voeg_ingredient_toe(Ingredient("gula djawa", 0.5, "el", kcal=20))
    recept2.voeg_ingredient_toe(Ingredient("zout", 0.25, "tl", kcal=0))    
    recept2.voeg_ingredient_toe(Ingredient("rijst", 75, "gram", kcal=263))

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
    recept3.voeg_ingredient_toe(Ingredient("hamlappen", 125, "gram", plantaardig_alternatief=PlantaardigAlternatief("tempeh", 170), kcal=300))
    recept3.voeg_ingredient_toe(Ingredient("knoflook", 1, "teen", kcal=5))
    recept3.voeg_ingredient_toe(Ingredient("ui", 1, "stuk", kcal=30))
    recept3.voeg_ingredient_toe(Ingredient("oestersaus", 0.5, "eetlepel", kcal=10))
    recept3.voeg_ingredient_toe(Ingredient("ketjap manis", 0.5, "eetlepel", kcal=15))
    recept3.voeg_ingredient_toe(Ingredient("sambal oelek", 0.25, "theelepel", kcal=1))
    recept3.voeg_ingredient_toe(Ingredient("gember", 1, "cm", kcal=2))
    recept3.voeg_ingredient_toe(Ingredient("palm suiker", 0.25, "theelepel", kcal=5))
    recept3.voeg_ingredient_toe(Ingredient("maizena", 0.25, "eetlepel", kcal=9))

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
    recept4.voeg_ingredient_toe(Ingredient("wortel", 0.5, "stuk", kcal=15))
    recept4.voeg_ingredient_toe(Ingredient("sperziebonen", 50, "gram", kcal=15))
    recept4.voeg_ingredient_toe(Ingredient("kousenband", 25, "gram", kcal=8))
    recept4.voeg_ingredient_toe(Ingredient("aubergine", 0.25, "stuk", kcal=6))
    recept4.voeg_ingredient_toe(Ingredient("courgette", 0.25, "stuk", kcal=5))
    recept4.voeg_ingredient_toe(Ingredient("kokosmelk", 100, "ml", kcal=200))
    recept4.voeg_ingredient_toe(Ingredient("sajoer lodeh boemboe", 0.25, "zakje", kcal=25))

    recepten.append(recept4)

    # Laat gebruiker kiezen welk recept
    print("Kies een recept uit de lijst:")
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r._Recept__naam}")
    keuze = input("Typ het nummer van het recept of 'alle' om alles te tonen: ").strip().lower()
    if keuze == 'alle':
        geselecteerde_recepten = recepten
    else:
        try:
            num = int(keuze)
            if 1 <= num <= len(recepten):
                geselecteerde_recepten = [recepten[num-1]]
            else:
                print("Ongeldig nummer, alle recepten worden getoond.")
                geselecteerde_recepten = recepten
        except ValueError:
            print("Ongeldige invoer, alle recepten worden getoond.")
            geselecteerde_recepten = recepten

    # Vraag het aantal personen (basis hoeveelheden zijn nu per persoon)
    try:
        aantal_personen = int(input("Voor hoeveel personen wil je het recept maken? "))
        if aantal_personen < 1:
            aantal_personen = 1
    except ValueError:
        aantal_personen = 1

    # Vraag of plantaardig alternatief gewenst is
    plantaardig = input("Wil je een plantaardige versie? (ja/nee): ").strip().lower() == "ja"

    # Print geselecteerde recepten met aangepaste hoeveelheden en kcal per persoon
    for recept in geselecteerde_recepten:
        print(f"\nIngrediënten voor {recept._Recept__naam} (voor {aantal_personen} personen):")
        totale_kcal_per_person = 0
        for ingredient in recept.get_ingredienten():
            # Bepaal welke naam gebruiken
            if plantaardig and ingredient.plantaardig_alternatief:
                naam = str(ingredient.plantaardig_alternatief)
                alternatief_str = " (plantaardig alternatief)"
            else:
                naam = ingredient.naam
                alternatief_str = ""

            # Bereken totale hoeveelheid voor het gekozen aantal personen
            try:
                hoeveelheid_per_person = float(ingredient.hoeveelheid)
                hoeveelheid_totaal = hoeveelheid_per_person * aantal_personen
                hoeveelheid_totaal = int(hoeveelheid_totaal) if float(hoeveelheid_totaal).is_integer() else round(hoeveelheid_totaal, 2)
            except (ValueError, TypeError):
                hoeveelheid_totaal = ingredient.hoeveelheid

            # Bereken kcal per persoon (ingredient.kcal is basis per persoon)
            try:
                kcal_per_person = float(ingredient.kcal)
            except (ValueError, TypeError):
                kcal_per_person = 0
            totale_kcal_per_person += kcal_per_person

            print(f"- {hoeveelheid_totaal} {ingredient.eenheid} {naam}{alternatief_str} [{int(kcal_per_person)} kcal p.p.]")

        print("Stappen:")
        for stap in recept.get_stappen():
            print(f"- {stap.beschrijving}")

        # Toon totale kcal per persoon (som van kcal per ingrediënt)
        print(f"Totale kcal per persoon: {int(totale_kcal_per_person)} kcal")


if __name__ == "__main__":
    main()
