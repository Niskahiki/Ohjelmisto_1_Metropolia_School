class Elevator:
    def __init__(self, lowest_floor: int, highest_floor: int):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def floor_up(self):
        if self.current_floor + 1 <= self.highest_floor:
            self.current_floor += 1

        print(f"Hissi on nyt kerroksessa: {self.current_floor}")

    def floor_down(self):
        if self.current_floor - 1 >= self.lowest_floor:
            self.current_floor -= 1

        print(f"Hissi on nyt kerroksessa: {self.current_floor}")

    def go_to_floor(self, floor_number: int):
        if floor_number == self.current_floor:
            print(f"Hissi on nyt kerroksessa: {self.current_floor}")

        elif floor_number > self.current_floor:
            difference = floor_number - self.current_floor

            for _ in range(0, difference):
                self.floor_up()

        elif floor_number < self.current_floor:
            difference = self.current_floor - floor_number

            for _ in range(0, difference):
                self.floor_down()


elevator1 = Elevator(1, 5)

elevator1.go_to_floor(5)
elevator1.go_to_floor(1)
