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


car1 = Car("abc-123", 142)

print(vars(car1))

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"Auton nopeus: {car1.current_speed}")

car1.accelerate(-200)

print(f"Auton nopeus: {car1.current_speed}")
