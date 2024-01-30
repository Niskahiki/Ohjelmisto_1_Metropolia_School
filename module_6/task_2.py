import random


def throw_dice(dice_sides: int) -> int:
    return random.randint(1, dice_sides)


def main():
    dice_sides = int(input("Kuinka monta nopan tahkoa: "))
    print(f"Heitän noppaa kunnes saan {dice_sides}.")

    while True:
        dice = throw_dice(dice_sides)

        print(dice)

        if dice == dice_sides:
            break


if __name__ == '__main__':
    main()
