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


class ElectricCar(Car):
    def __init__(self, license_plate: str, top_speed: int, battery_capacity: float):
        super().__init__(license_plate, top_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, license_plate: str, top_speed: int, fuel_capacity: float):
        super().__init__(license_plate, top_speed)
        self.fuel_capacity = fuel_capacity


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(125)
    gasoline_car.accelerate(132)

    electric_car.move(3)
    gasoline_car.move(3)

    print(f"Sähköauton mittarilukema: {electric_car.mileage}km")
    print(f"Polttorimoottoriauton mittarilukema: {gasoline_car.mileage}km")


if __name__ == "__main__":
    main()
