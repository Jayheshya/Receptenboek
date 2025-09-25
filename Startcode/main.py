
from recept import Recept, Ingredient
from stap import Stap

def main():


    recepten = []

    # Maak een nieuw recept aan
    recept1 = Recept("Kwetiau Ayam", "Gewokte rijstnoedels met kip en chinese kool.")

    # Voeg ingrediënten toe
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("chinese kool", 400, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("kwetiau rijstnoedels", 250, "gram"))

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
    recept2.voeg_ingredient_toe(Ingredient("rendang boemboe", 1, "stuk"))
    recept2.voeg_ingredient_toe(Ingredient("sucadelappen", 1, "kilo"))
    recept2.voeg_ingredient_toe(Ingredient("kokosmelk", 400, "ml"))
    recept2.voeg_ingredient_toe(Ingredient("water", 200, "ml"))
    recept2.voeg_ingredient_toe(Ingredient("laos", 2, "cm"))
    recept2.voeg_ingredient_toe(Ingredient("sereh", 2, "stengels"))
    recept2.voeg_ingredient_toe(Ingredient("kaneel", 1, "stokje"))
    recept2.voeg_ingredient_toe(Ingredient("gula djawa", 2, "el"))
    recept2.voeg_ingredient_toe(Ingredient("zout", 1, "tl"))    
    recept2.voeg_ingredient_toe(Ingredient("rijst", 300, "gram"))

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
    recept3.voeg_ingredient_toe(Ingredient("hamlappen", 500, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("knoflook", 1, "teen"))
    recept3.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))
    recept3.voeg_ingredient_toe(Ingredient("oestersaus", 2, "eetlepels"))
    recept3.voeg_ingredient_toe(Ingredient("ketjap manis", 2, "eetlepels"))
    recept3.voeg_ingredient_toe(Ingredient("sambal oelek", 1, "theelepel"))
    recept3.voeg_ingredient_toe(Ingredient("gember", 1, "cm"))
    recept3.voeg_ingredient_toe(Ingredient("palm suiker", 1, "theelepel"))
    recept3.voeg_ingredient_toe(Ingredient("maizena", 1, "eetlepel"))

    recept3.voeg_stap_toe(Stap("Snij de hamlappen in dunne repen en marineer het met de rest van ingrediënten voor de marinade."))
    recept3.voeg_stap_toe(Stap("Laat het vlees nu minimaal 1 uur of langer marineren."))
    recept3.voeg_stap_toe(Stap("Bak het vlees in een klein beetje olie in een ruime koekenpan totdat het goudbruin is."))
    recept3.voeg_stap_toe(Stap("Maak tegelijkertijd de saus door het uitje fijn te snipperen."))
    recept3.voeg_stap_toe(Stap("Verhit een beetje olie in een steelpan met dikke bodem en fruit het uitje aan tot deze zacht en glazig is."))
    recept3.voeg_stap_toe(Stap("Knijp dan de knoflookteentjes uit en voeg deze toe. Bak even kort mee."))
    recept3.voeg_stap_toe(Stap("Maak een papje van de maizena met een beetje water en voeg dit toe aan het uitje en knoflook."))
    recept3.voeg_stap_toe(Stap("Serveer de saus over de stukjes gebakken varkensvlees eventueel met een beetje atjar tjampoer, rijst en komkommer erbij."))
                                       
    recepten.append(recept3)



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
