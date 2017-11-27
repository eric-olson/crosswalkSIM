
import queue
from enum import Enum

class StoplightState(Enum):
    RED = 1
    YELLOW = 2
    # initial green state after red has expired
    GREEN = 3
    # green timer has expired, next button press will trigger yellow
    GREEN_EXPIRED = 4
    # button has been pushed, waiting for green timer to expire
    GREEN_WAITING = 5

class Road:
    def __init__(self, current_time, t_red, t_yellow, t_green):
        # store current time
        self.last_update = current_time

        # time values for red/yellow/green
        self.t_red = t_red
        self.t_yellow = t_yellow
        self.t_green = t_green

        # start timer at green
        self.timer = t_green

        # initial stoplight state is GREEN_EXPIRED
        self.stoplight = StoplightState.GREEN_EXPIRED

        # each road direction is a queue
        self.east = []
        self.west = []

        # crosswalk is represented as a queue
        self.crosswalk = queue.Queue()

        print ("[ROAD] created at time {}".format(current_time))

    def add_auto(self, auto):
        # add a vehicle to correct road direction (even east, odd west)
        if (auto.num % 2 == 0):
            print ("[ROAD] adding vehicle to east lane")
            self.east.append(auto)
        else:
            print ("[ROAD] adding vehicle to west lane")
            self.west.append(auto)

    def add_ped(self, ped):
        # add a pedestrian to correct road direction
        return
