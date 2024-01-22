cabin_class = input("Mikä on hytti luokkasi?: ")

if cabin_class.lower() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabin_class.lower() == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabin_class.lower() == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabin_class.lower() == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")