
city_list: [str] = []
for i in range(5):
    city = input("Anna jokin kaupungin nimi: ")

    if city not in city_list:
        city_list.append(city)
    else:
        print("Kaupunki on jo listalla. Kaupunkia ei lisätty.")

for city in city_list:
    print(city)