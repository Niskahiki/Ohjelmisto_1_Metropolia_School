username = "python"
password = "rules"

times_tried = 1

while times_tried <= 5:
    input_username = input("\nAnna käyttäjätunnus: ")
    input_password = input("Anna salasana: ")

    if input_username == username and input_password == password:
        print("\nTervetuloa")
        break
    else:
        print("\nPääsy evätty")
        times_tried += 1