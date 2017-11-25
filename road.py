
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
    def __init__(self, t_red, t_yellow, t_green):
        # time values for red/yellow/green
        self.t_red = t_red
        self.t_yellow = t_yellow
        self.t_green = t_green

        # start timer at green
        self.timer = t_green
        # initial stoplight state is GREEN_EXPIRED
        self.stoplight = StoplightState.GREEN_EXPIRED

        # each road direction is a queue
        self.road_east = queue.Queue()
        self.road_west = queue.Queue()

        # crosswalk is represented as a queue
        self.crosswalk = queue.Queue()

