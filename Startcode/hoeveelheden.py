def pas_hoeveelheden_aan(ingredienten, aantal_personen, standaard_personen=4):
    """
    Past de hoeveelheden van de ingrediënten aan op basis van het aantal personen.
    ingredienten: lijst van Ingredient-objecten
    aantal_personen: gewenst aantal personen
    standaard_personen: standaard aantal personen waarop het recept is gebaseerd (default=4)
    Geeft een lijst van strings terug met aangepaste hoeveelheden.
    """
    factor = aantal_personen / standaard_personen
    aangepaste_lijst = []
    for ingredient in ingredienten:
        try:
            nieuwe_hoeveelheid = float(ingredient.hoeveelheid) * factor
            # Toon als geheel getal indien mogelijk
            if nieuwe_hoeveelheid.is_integer():
                nieuwe_hoeveelheid = int(nieuwe_hoeveelheid)
        except ValueError:
            nieuwe_hoeveelheid = ingredient.hoeveelheid
        aangepaste_lijst.append(f"{nieuwe_hoeveelheid} {ingredient.eenheid} {ingredient.naam}")
    return aangepaste_lijst
