getal1 = float(input("Voer het eerste getal in: "))
operator = input("Voer een operator (+, -) in: ")
getal2 = float(input("Voer het tweede getal in: "))

if operator == "+":
    resultaat = getal1 + getal2
else:
    resultaat = getal1 - getal2

print(resultaat)
