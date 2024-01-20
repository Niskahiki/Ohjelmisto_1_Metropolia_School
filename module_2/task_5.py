leviskat = float(input("Anna leviskät: "))
print()
naulat = float(input("Anna naulat: "))
print()
luodit = float(input("Anna luodit: "))
print()

naulat += leviskat * 20
luodit += naulat * 32

grams = luodit * 13.3

kg_str = str(grams / 1000)

kg, grams_string = kg_str.split(".")

print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {int(grams_string)/100} grammaa.")