
def gallons_to_liters(gallons) -> float:
    return gallons * 3.785


def main():
    while True:
        usr_gallons = float(input("Anna nestegallonien määrä. Negatiivinen luku päättää ohjelman: "))

        if usr_gallons < 0:
            break
        else:
            liters = gallons_to_liters(usr_gallons)
            print(f"{usr_gallons} nestegallonia litroina on {liters:.2f}l.")


if __name__ == '__main__':
    main()
