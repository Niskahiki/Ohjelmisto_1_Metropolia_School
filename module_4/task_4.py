import random

random_integer = random.randint(1, 10)

print("Arvoin luvun väliltä 1-10, arvaa luku.")
while True:
    guess = input("\nAnna arvaus: ")

    if guess.isnumeric():
        guess = int(guess)
        if 1 <= guess <= 10:
            if guess > random_integer:
                print("Liian suuri arvaus.")

            elif guess < random_integer:
                print("Liian pieni arvaus")

            else:
                print(f"Arvasit oikein. Luku oli: {random_integer}.")
                break
        else:
            print(f"Luku {guess} on liian suuri tai pieni. Arvaa luku väliltä 1-10.")
    else:
        print(f"Huono arvaus '{guess}'.\nAnna arvaus kokonaislukuna väliltä 1-10")