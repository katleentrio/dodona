# Vraag de gebruiker om het factuurbedrag
factuurbedrag = float(input("Voer het factuurbedrag in: "))

# Controleer het factuurbedrag en bereken de korting
if factuurbedrag > 100:
    korting = factuurbedrag * 0.05
else:
    korting = factuurbedrag * 0.03

# Bereken het bedrag na korting
bedrag_na_korting = factuurbedrag - korting

# Print het bedrag na korting
print("Het bedrag na korting is: ", bedrag_na_korting)

# Print de korting
print("De korting is:", korting)



# Print het bedrag na korting
print("Het bedrag na korting is: ", bedrag_na_korting)
