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


class Race:

    def __init__(self, name: str, km_length: float, racers: [Car]):
        self.name = name
        self.km_length = km_length
        self.racers: [Car] = racers

    def hour_pass(self):
        for car in self.racers:
            acceleration = randint(-10, 15)
            car.accelerate(acceleration)
            car.move(1)

    def print_score(self):
        current_car_scores = sorted(self.racers, key=lambda c: c.mileage, reverse=True)  # Sort table. First == largest mileage

        console = Console()

        race_table = Table(show_header=True)

        race_table.add_column("ranking")
        race_table.add_column("license plate")
        race_table.add_column("top speed")
        race_table.add_column("current speed")
        race_table.add_column("mileage")

        for i in range(0, len(current_car_scores)):
            race_table.add_row(
                str(i + 1) + ".",
                current_car_scores[i].license_plate,
                str(current_car_scores[i].top_speed) + " km/h",
                str(current_car_scores[i].current_speed) + " km/h",
                str(current_car_scores[i].mileage) + " km"
            )

        console.print(race_table)

    def is_race_over(self):
        for car in self.racers:
            if car.mileage >= self.km_length:
                return True

        return False


def main():
    race_cars = []

    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        top_speed = randint(100, 200)
        race_cars.append(Car(license_plate, top_speed))

    race1 = Race("Suuri romuralli", 8000, race_cars)

    time_from_last_score_print = 0
    while True:
        race1.hour_pass()
        if race1.is_race_over():
            race1.print_score()
            break

        time_from_last_score_print += 1

        if time_from_last_score_print >= 10:
            race1.print_score()
            time_from_last_score_print = 1


if __name__ == "__main__":
    main()
