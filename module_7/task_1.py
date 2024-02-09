def main():
    season_months = (
        "Talvi", "Talvi", "Kevät",
        "Kevät", "Kevät", "Kesä",
        "Kesä", "Kesä", "Syksy",
        "Syksy", "Syksy", "Talvi"
    )

    usr_input = int(input("Anna kuukauden numero: ")) - 1

    if 0 < usr_input < len(season_months):
        print(f"Antamasi kuukausi kuuluu {season_months[usr_input]} kauteen.")
    else:
        print("Antamasi kuukauden numero ei ole olemassa.")


if __name__ == '__main__':
    main()