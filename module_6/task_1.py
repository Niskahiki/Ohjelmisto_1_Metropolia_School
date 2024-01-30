import random


def throw_dice() -> int:
    return random.randint(1, 6)


def main():
    print("Heitetään noppaa kunnes tulee luku 6.")

    while True:
        dice = throw_dice()

        print(dice)

        if dice == 6:
            break


if __name__ == '__main__':
    main()
