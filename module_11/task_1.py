class Release:
    def __init__(self, name: str):
        self.name = name


class Book(Release):
    def __init__(self, name: str, writer: str, pages: int):
        super().__init__(name)
        self.writer = writer
        self.pages = pages

    def print_values(self):
        print(f"Kirjan nimi: {self.name}, kirjoittaja: {self.writer} ja sivumäärä: {self.pages}")


class Magazine(Release):
    def __init__(self, name: str, editor_in_chief: str):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_values(self):
        print(f"Lehden nimi: {self.name} ja päätoimittaja: {self.editor_in_chief}")


def main():
    magazine1 = Magazine("Aku Ankka", "Aki Hyyppä")
    book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)

    magazine1.print_values()
    book1.print_values()


if __name__ == "__main__":
    main()
