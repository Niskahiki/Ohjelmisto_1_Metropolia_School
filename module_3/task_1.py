fish_length = float(input("Anna kuhan pituus senttimetreinä: "))

if fish_length < 37:
    missing_length = 37 - fish_length
    print("Kuha on liian pieni. Päästä kuha takaisin.")
    print(f"Kuhan alimmasta salitusta pyyntimitasta puuttuu: {missing_length:.2f}cm")
else:
    print("Kuhan pituus on sopiva.")