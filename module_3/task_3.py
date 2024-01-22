biological_gender = input("Mikä on biologinen sukupuolesi (nainen/mies)?: ")
hemoglobin_value = float(input("Mikä on hemoglobiiniarvosi (g/l)?: "))

if biological_gender.lower() in ("nainen", "mies"):
    if biological_gender == "nainen":
        if 117 <= hemoglobin_value <= 175:
            print("Hemoglobiiniarvosi on normaali.")
        elif hemoglobin_value > 175:
            print("Hemoglobiiniarvosi on korkea.")
        else:
            print("Hemoglobiiniarvosi on alhainen.")
    else:
        if 134 <= hemoglobin_value <= 195:
            print("Hemoglobiiniarvosi on normaali.")
        elif hemoglobin_value > 195:
            print("Hemoglobiiniarvosi on korkea.")
        else:
            print("Hemoglobiiniarvosion on alhainen.")

else:
    print(f"{biological_gender} ei ole ohjelmassa toimiva sukupuoli.")