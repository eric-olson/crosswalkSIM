
import math
from enum import Enum

import auto
import pedestrian

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

    sim.road.add_auto(new_auto)

    # compute expected exit time
    # TODO: store this for welford reasons probably
    new_auto.calc_travel_time(sim.road_length)

    # precompute time at crosswalk
    new_auto.calc_crosswalk_time(sim.distance_to_crosswalk, sim.crosswalk_width)

    # create next arrival event
    uniform = sim.auto_tr.get_next()
    exponential = -1 * sim.auto_mu * math.log(uniform)
    next_time = sim.time + exponential
    next_id = auto_id + 2

    if next_id <= sim.n:
        next_arrival = (next_time, auto_arrival, (next_id, ))
        sim.q.put(next_arrival)

    return


def ped_arrival(sim, ped_id):
    print("[EVENT] ped_arrival")
    # create pedestrian and add to queue
    new_ped = pedestrian.Pedestrian(ped_id,
                                    sim.ped_speed_prng,
                                    sim.time)

    sim.road.add_ped(new_ped)

    # calculate time to arrive at button & create event
    arrive_at_crosswalk = new_ped.calc_crosswalk_time(sim.block_width)
    button_event = (arrive_at_crosswalk, ped_at_button, (ped_id, ))

    # precompute total expected travel time, minus delay
    new_ped.calc_travel_time(sim.block_width + sim.street_width)

    # create next arrival event
    uniform = sim.ped_tr.get_next()
    exponential = -1 * sim.ped_mu * math.log(uniform)
    next_time = sim.time + exponential
    next_id = ped_id + 2

    if next_id <= sim.n:
        next_arrival = (next_time, ped_arrival, (next_id, ))
        sim.q.put(next_arrival)

    return


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
