def search_airport_from_airports_set(airports_set: set, airport_code: str) -> tuple or None:
    for airport in airports_set:
        if airport[0] == airport_code:
            return airport
    else:
        return None


def main():
    airports_set = set()

    while True:
        print("\n" + '-' * 20 + "\n")
        usr_choice = input("Valitse toiminto:"
                           "\n(0) Lisää lentokenttä."
                           "\n(1) Hae lisättyä lentokenttää."
                           "\n(2) Lopeta ohjelma."
                           "\n\nHaluttu toiminto: ")

        match usr_choice:

            case "0":
                airport_code = input("\nAnna lentokentän ICAO-koodi: ")
                airport_name = input("Anna lentokentän nimi: ")

                if airport_code == "":
                    print("\nLentokentän ICAO-koodi ei voi olla tyhjä.")
                elif airport_name == "":
                    print("\nLentokentän nimi ei voi olla tyhjä.")
                else:
                    does_airport_already_exist = search_airport_from_airports_set(airports_set, airport_code)

                    if does_airport_already_exist:
                        print("\nLentokenttä annetulla ICAO-koodilla on jo olemassa.\nUutta lentokenttää ei lisätty.")
                    else:
                        airports_set.add((airport_code, airport_name))
                        print("\nUusi lentokenttä lisätty.")

            case "1":
                airport_code = input("\nAnna haettavan lentokentän ICAO-koodi: ")

                searched_airport = search_airport_from_airports_set(airports_set, airport_code)

                if searched_airport:
                    print(f"\nICAO-koodilla '{searched_airport[0]}' löytyi, '{searched_airport[1]}' niminen lentokenttä.")
                else:
                    print(f"\nICAO-koodilla '{airport_code}' ei löytynyt yhtään lentokenttää.")

            case "2":
                print("\nLopetetaan...")
                break

            case _:
                print("\nVirheellinen syöte.")


if __name__ == "__main__":
    main()
