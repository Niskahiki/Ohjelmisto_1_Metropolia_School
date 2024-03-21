class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.mileage = 0


car1 = Car("abc-123", 142)

print(vars(car1))
