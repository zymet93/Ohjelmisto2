# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Elevator:
    def __init__(self, elevator_num, bottom_floor, top_floor):
        self.elevator_num = elevator_num
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f'Elevator {self.elevator_num} goes up to the floor {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f'Elevator {self.elevator_num} goes down to the floor {self.current_floor}')

    def go_to_floor(self, floor):
        if floor >= self.bottom_floor and floor <= self.top_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            print(f"Elevator {self.elevator_num} has reached floor {floor}")
        else:
            print("Invalid floor number")

class Building:
    def __init__(self, elevators, bottom_num, top_num):
        self.bottom_num = bottom_num
        self.top_num = top_num
        self.elevators = [Elevator(i, bottom_num, top_num) for i in range(1, elevators + 1)]
#lisätty elevator number run_elevator
    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number - 1].go_to_floor(destination)
    #palohälytys
    def fire_alarm(self):
        print("Fire alarm activated. All elevators going to ground floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_num)


#Building (Hissien määrä,botfloor,topfloor)
new_Building = Building(3, 0, 10)

#elevator run floor values

new_Building.run_elevator(1, 5) # hissi #1 kerrokseen 5
new_Building.run_elevator(2, 7) # hissi #2 kerrokseen 7

# Palohälytys laukeaa
new_Building.fire_alarm()


