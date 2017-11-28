
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

        # road is a dictionary keyed on auto ID
        self.road = {}
        # sidewalk is a dictionary keyed on pedestrian ID
        self.sidewalk = {}

        # crosswalk is represented as a queue
        self.crosswalk = queue.Queue()
        self.too_slow = queue.Queue()

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
            self.last_walk = time

    def red_light(self, time):
        print("[ROAD] red light started")
        # store start time of red light
        self.last_red = time
        # determine pedestrian crossings. don't have to worry about slow peds
        # in this part- only if a pedestrian arrives during a walk signal
        max_crossings = 20
        self.remaining_crossings = 0
        ped_delays = []
        for x in range(0, max_crossings):
            if self.crosswalk.empty():
                # store remaining allowed pedestrian crossings
                self.remaining_crossings = max_crossings - x
                break;
            ped = self.crosswalk.get()
            print("[ROAD] telling pedestrian {} to cross street".format(ped.num))
            delay = ped.cross_street(time)
            ped_delays.append(delay)

        print("[ROAD] {} peds can still cross street".format(self.remaining_crossings))

        # determine if vehicles will be delayed
        print("[ROAD] checking vehicles for delay")
        for num, auto in self.road.items():
            auto.red_light(time, self.t_red)

        return ped_delays

    def green_light(self):
        # move too_slow members to main crosswalk queue
        print("[ROAD] moving too_slow peds to crosswalk")
        while not self.too_slow.empty():
            ped = self.too_slow.get()
            self.crosswalk.put(ped)

    def add_auto(self, auto):
        # add a vehicle to road dictionary
        print ("[ROAD] adding vehicle to road")
        self.road[auto.num] = auto

    def add_ped(self, ped):
        # add pedestrian to sidewalk dictionary
        print ("[ROAD] adding ped to sidewalk")
        self.sidewalk[ped.num] = ped

    def ped_arrives(self, ped_id, time):
        print("[ROAD] ped has arrived at crosswalk")
        # move ped from sidewalk to crosswalk queue
        ped = self.sidewalk.pop(ped_id)

        # cross street if allowed
        if self.state == StoplightState.RED and self.crosswalk.empty():
            remaining_time = time - self.last_red
            print("[ROAD] stoplight is red, checking if ped can cross in {} s".format(remaining_time))
            if ped.cross_time < remaining_time:
                print("[ROAD] telling ped #{} to cross street".format(ped_id))
                delay = ped.cross_street(time)
                return delay
            else:
                print("[ROAD] not enough time for ped #{} to cross street".format(ped_id))
                self.too_slow.put(ped)
        else:
            print("[ROAD] moving ped #{} to crosswalk".format(ped_id))
            self.crosswalk.put(ped)


    def num_peds_waiting(self):
        return self.crosswalk.qsize()

