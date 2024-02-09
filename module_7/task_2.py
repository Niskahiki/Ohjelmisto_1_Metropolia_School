def main():
    name_set = set()

    while True:
        usr_name = input("Anna jokin nimi (Tyhjä pysäyttää ohjelman): ")

        if usr_name == "":
            break

        if usr_name in name_set:
            print("Aiemmin syötetty nimi.\n")

        else:
            name_set.add(usr_name)
            print("Uusi nimi.\n")

    print("Lopetetaan...\n")
    for name in name_set:
        print(name)


if __name__ == '__main__':
    main()
