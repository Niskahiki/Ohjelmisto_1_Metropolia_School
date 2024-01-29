usr_num = int(input("Anna jokin kokonais luku, niin kerron onko se alkuluku: "))

for i in range(2, usr_num):
    if usr_num % i == 0:
        print(f"{usr_num} ei ole alkuluku. Luku on jaollinen luvulla: {i}")
        break

    if i == usr_num - 1:
        print(f"{usr_num} on alkuluku.")