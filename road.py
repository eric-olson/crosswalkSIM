
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

        self.last_walk = current_time

        # time values for red/yellow/green
        self.t_red = t_red
        self.t_yellow = t_yellow
        self.t_green = t_green

        # start timer at green (TODO: is timer storage even necessary?)
        self.timer = t_green

        # initial stoplight state is GREEN_EXPIRED
        self.state = StoplightState.GREEN_EXPIRED

        # each road direction
        self.east_road = []
        self.west_road = []
        # sidewalk is a dictionary keyed on pedestrian ID
        self.sidewalk = {}

        # crosswalk is represented as a queue
        self.crosswalk = queue.Queue()

        print ("[ROAD] created at time {}".format(current_time))

    def push_button(self, time):
        print("[ROAD] button pushed at time {}".format(time))

        if self.state == StoplightState.GREEN:
            print("[ROAD] changing state to GREEN_WAITING")
            self.update_state(StoplightState.GREEN_WAITING, time)
            return self.state

        elif self.state == StoplightState.GREEN_EXPIRED:
            print("[ROAD] changing light to yellow")
            self.update_state(StoplightState.YELLOW, time)
            return self.state

        else:
            print("[ROAD] no state change")

        return

    def update_state(self, new_state, time):
        # TODO: add check for illegal state transitions?

        print("[ROAD] changing state to {}".format(new_state))
        self.state = new_state
        self.last_update = time

        # store the end time of the last walk signal
        if new_state == StoplightState.GREEN:
            last_walk = time

    def red_light(self, time):
        # determine pedestrian crossings
        max_crossings = 20

        # TODO: determine vehicle delays

    def add_auto(self, auto):
        # add a vehicle to correct road direction (even east, odd west)
        if (auto.num % 2 == 0):
            print ("[ROAD] adding vehicle to east lane")
            self.east_road.append(auto)
        else:
            print ("[ROAD] adding vehicle to west lane")
            self.west_road.append(auto)

    def add_ped(self, ped):
        # add pedestrian to sidewalk dictionary
        print ("[ROAD] adding ped to sidewalk")
        self.sidewalk[ped.num] = ped

    def ped_arrives(self, ped_id):
        print("[ROAD] moving ped #{} to crosswalk".format(ped_id))
        # move ped from sidewalk to crosswalk queue
        ped = self.sidewalk.pop(ped_id)
        self.crosswalk.put(ped)

    def num_peds_waiting(self):
        return self.crosswalk.qsize()

