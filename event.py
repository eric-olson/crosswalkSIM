
import math
from enum import Enum

import auto

class Event(Enum):
    AUTO_ARRIVAL = 1
    PED_ARRIVAL = 2
    PED_AT_BUTTON = 3
    PED_IMPATIENT = 4
    GREEN_EXPIRES = 5
    YELLOW_EXPIRES = 6
    RED_EXPIRES = 7
    AUTO_EXIT = 8
    PED_EXIT = 9

def auto_arrival(sim, auto_id):
    print("[EVENT] auto_arrival")

    # add new auto to queue (what about direction?)
    new_auto = auto.Auto(auto_id,
                         sim.auto_speed_prng,
                         sim.time,
                         sim.auto_accel)

    sim.road.add_vehicle(new_auto)

    # compute expected exit time
    # TODO: store this for welford reasons probably
    new_auto.calc_travel_time(sim.road_length)

    # precompute time at crosswalk
    new_auto.calc_crosswalk_time(sim.distance_to_crosswalk, sim.crosswalk_width)

    # create next arrival event
    uniform = sim.auto_tr.get_next()
    exponential = -1 * sim.auto_mu * math.log(uniform)
    next_time = sim.time + exponential

    if auto_id < 10:
        next_arrival = (next_time, auto_arrival, (auto_id + 2, ))
        sim.q.put(next_arrival)

    return


def ped_arrival(sim, ped_id):
    # calculate time to arrive at button & create event

    # precompute total travel time, minus delay

    print("[EVENT] ped_arrival")

def ped_at_button(sim, ped_id):
    # determine if pedestrian will push button

    # create impatient event

    print("[EVENT] ped_at_button")

def ped_impatient(sim, ped_id):
    # check if ped has crossed the street yet

    # push the button

    print("[EVENT] ped_impatient")

def green_expires(sim):
    # update state based on if walk button has been pushed

    print("[EVENT] green_expires")

def yellow_expires(sim):
    # update state

    # delay vehicles that would be in the crosswalk

    print("[EVENT] yellow_expires")

def red_expires(sim):
    # update state

    # clean up crosswalk? what needs to be done here?

    print("[EVENT] red_expires")

def auto_exit(sim, auto_id):
    # store total travel time

    # remove auto from simulation

    print("[EVENT] auto_exit")

def ped_exit(sim, ped_id):
    # store total travel time

    # remove ped from simulation

    print("[EVENT] ped_exit")
