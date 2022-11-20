import time
from enum import Enum
from typing import List
from typing import Dict


class EntryData:
    def __init__(self, x_coordinate: int, width: int, height: int):
        self.x_coordinate = x_coordinate
        self.width = width
        self.height = height

    def __str__(self):
        return f"({self.x_coordinate}; {self.width}; {self.height})"


class Position:

    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x

    def __str__(self):
        return f"({self.x}; {self.y})"


class Directions(Enum):
    FRONT = 1
    BACK = 2
    UP = 3
    DOWN = 4
    NONE = 5


class Drone:
    building_counter = 0
    previous_step = Directions.NONE
    position = Position(0, 0)
    vision: Dict[Directions, Position] = {}
    # vision = {}
    PREDETERMINED_HEIGHT = 3

    def __init__(self, input_data: List[EntryData]):
        self.input_data = input_data
        self.vision[Directions.FRONT] = Position(0, 0)
        self.vision[Directions.BACK] = Position(0, 0)
        self.vision[Directions.UP] = Position(0, 0)
        self.vision[Directions.DOWN] = Position(0, 0)

    def update_vision_position(self):
        self.vision[Directions.FRONT].x = self.position.x + 3
        self.vision[Directions.FRONT].y = self.position.y
        self.vision[Directions.BACK].x = self.position.x - 3
        self.vision[Directions.BACK].y = self.position.y
        self.vision[Directions.UP].x = self.position.x
        self.vision[Directions.UP].y = self.position.y + 3
        self.vision[Directions.DOWN].x = self.position.x
        self.vision[Directions.DOWN].y = self.position.y - 3

    def move_forward(self):
        self.position.x = self.position.x + 1
        self.update_vision_position()

    def move_up(self):
        self.position.y = self.position.y + 1
        self.update_vision_position()

    def move_down(self):
        if self.position.y > self.PREDETERMINED_HEIGHT:
            self.position.y = self.position.y - 1
            self.update_vision_position()
        else:
            self.building_counter = self.building_counter + 1

    def force_move_down(self):
        self.position.y = self.position.y - 1
        self.update_vision_position()

    def scan(self):
        y_building = self.input_data[self.building_counter].height
        x_building_first_wall = self.input_data[self.building_counter].x_coordinate
        x_building_second_wall = self.input_data[self.building_counter].x_coordinate + self.input_data[
            self.building_counter].width
        if (self.vision[Directions.FRONT].x == x_building_first_wall) and (self.vision[Directions.DOWN].y < y_building):
            return Directions.FRONT
        elif (self.vision[Directions.DOWN].y == y_building) and (
                self.vision[Directions.BACK].x < x_building_second_wall):
            return Directions.DOWN
        elif self.vision[Directions.BACK].x == x_building_second_wall:
            return Directions.BACK
        else:
            return Directions.NONE


def parse_file(filename: str):
    data: List[EntryData] = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            values = line.split()
            # values = [int(i) for i in values ]
            data.append(EntryData(int(values[0]), int(values[1]), int(values[2])))
    return data


if __name__ == '__main__':

    entry_data = parse_file("data.txt")
    drone = Drone(entry_data)
    drone.scan()
    print("Drone started...")

    while drone.building_counter <= len(entry_data) - 1:
        if drone.position.y < drone.PREDETERMINED_HEIGHT:
            drone.move_up()
            print("Current coordinates: ", drone.position)
            continue

        direction = drone.scan()
        if direction == Directions.FRONT:
            drone.move_up()
            drone.previous_step = Directions.FRONT
        elif direction == Directions.BACK:
            drone.move_down()
            drone.previous_step = Directions.BACK
        elif direction == Directions.DOWN:
            drone.move_forward()
            drone.previous_step = Directions.DOWN
        elif direction == Directions.NONE:
            if drone.previous_step == Directions.BACK:
                drone.move_down()
            else:
                drone.move_forward()
            drone.previous_step = Directions.NONE

        time.sleep(0.2)
        print("Current coordinates: ", drone.position)

    for i in range(3):
        drone.force_move_down()
        time.sleep(0.2)
        print("Current coordinates: ", drone.position)

    print("Mission completed")








# class syntax
