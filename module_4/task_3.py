smallest: int or None = None
largest: int or None = None

while True:
    user_input = input("\nAnna jokin luku (tyhjä pysäyttää ohjelman): ")
    if user_input.isnumeric():
        user_input = int(user_input)
        if smallest is None or smallest > user_input:
            smallest = user_input

        if largest is None or largest < user_input:
            largest = user_input

    elif user_input == "":
        print("Lopetetaan...")
        print(f"Pienin = {smallest or 0}, Isoin = {largest or 0}")
    else:
        print(f"Virheellinen syöte '{user_input}'. \nAnnetun luvun pitää olla kokonais luku tai tyhjä")
