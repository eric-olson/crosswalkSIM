
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
        self.state = StoplightState.GREEN_EXPIRED

        # each road direction
        self.east_road = []
        self.west_road = []
        # each sidewalk direction
        self.east_sidewalk = []
        self.west_sidewalk = []

        # crosswalk is represented as a queue
        self.crosswalk = queue.Queue()

        print ("[ROAD] created at time {}".format(current_time))

    def add_auto(self, auto):
        # add a vehicle to correct road direction (even east, odd west)
        if (auto.num % 2 == 0):
            print ("[ROAD] adding vehicle to east lane")
            self.east_road.append(auto)
        else:
            print ("[ROAD] adding vehicle to west lane")
            self.west_road.append(auto)

    def add_ped(self, ped):
        # add a pedestrian to correct road direction (even east, odd west)
        if (ped.num % 2 == 0):
            print ("[ROAD] adding ped to east side")
            self.east_sidewalk.append(ped)
        else:
            print ("[ROAD] adding ped to west side")
            self.west_sidewalk.append(ped)
        return

    def num_peds_waiting(self):
        return len(crosswalk)
