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


class House:

    def __init__(self, lowest_floor: int, top_floor: int, count_of_elevators: int):
        self.lowest_floor = lowest_floor
        self.top_floor = top_floor
        self.elevators: [Elevator] = self.create_elevator_list(count_of_elevators)

    def create_elevator_list(self, count_of_elevators) -> [Elevator]:
        list_of_elevators = []
        for _ in range(0, count_of_elevators):
            list_of_elevators.append(Elevator(self.lowest_floor, self.top_floor))

        return list_of_elevators

    def drive_lift(self, elevator_number: int, destination_floor: int):
        if elevator_number < 1:
            print(f"Hissiä numerolla: {elevator_number}. Ei löytynyt.")
            return

        if elevator_number > len(self.elevators):
            print(f"Hissiä numerolla: {elevator_number}. Ei löytynyt.")
            return

        elevator = self.elevators[elevator_number-1]

        elevator.go_to_floor(destination_floor)


h = House(1, 10, 4)

h.drive_lift(2, 7)
