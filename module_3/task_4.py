year = int(input("Anna vuosi: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} on karkausvuosi")
        else:
            print(f"{year} ei ole karkausvuosi")
    else:
        print(f"{year} on karkausvuosi")
else:
    print(f"{year} ei ole karkausvuosi")