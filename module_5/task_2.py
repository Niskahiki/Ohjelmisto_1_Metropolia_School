num_list: [int] = []

while True:
    usr_input = input("Anna jokin luku. Tyhjä päättää ohjelman: ")

    if usr_input == "":
        num_list.sort(reverse=True)
        if len(num_list) >= 1:
            print(num_list[0:5])
        else:
            print([])

        break

    num_list.append(int(usr_input))
