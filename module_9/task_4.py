from random import randint
from rich.console import Console
from rich.table import Table

class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.mileage = 0

    def accelerate(self, acceleration: int):
        if acceleration > 0:
            if self.current_speed + acceleration >= self.top_speed:
                self.current_speed = self.top_speed
                return

            self.current_speed += acceleration

        if acceleration < 0:
            if self.current_speed + acceleration <= 0:
                self.current_speed = 0
                return

            self.current_speed += acceleration

    def move(self, hours: float):
        if hours <= 0:
            return

        self.mileage += self.current_speed * hours


def print_race_table(race_cars: list[Car]):
    race_cars.sort(key=lambda c: c.mileage, reverse=True)  # Sort table. First == largest mileage

    console = Console()

    race_table = Table(show_header=True)

    race_table.add_column("ranking")
    race_table.add_column("license plate")
    race_table.add_column("top speed")
    race_table.add_column("current speed")
    race_table.add_column("mileage")

    for i in range(0, len(race_cars)):
        race_table.add_row(
            str(i+1)+".",
            race_cars[i].license_plate,
            str(race_cars[i].top_speed)+" km/h",
            str(race_cars[i].current_speed)+" km/h",
            str(race_cars[i].mileage)+" km"
        )

    console.print(race_table)


def main():
    race_cars = []

    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        top_speed = randint(100, 200)
        race_cars.append(Car(license_plate, top_speed))

    while True:
        found_winner = False
        for car in race_cars:
            acceleration = randint(-10, 15)
            car.accelerate(acceleration)
            car.move(1)

            if car.mileage >= 10_000:
                found_winner = True
                break

        if found_winner:
            break

    print_race_table(race_cars)


if __name__ == "__main__":
    main()
