
import math
from enum import Enum

import auto
import pedestrian
from road import StoplightState

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
    sim.q.put(button_event)

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
    print("[EVENT] ped_at_button")

    # determine if pedestrian will push button
    print("[EVENT] stoplight state: {}".format(sim.road.state))
    # case 1: stoplight state is not red -> crosswalk is NO WALK
    if sim.road.state != StoplightState.RED:
        num_waiting = sim.road.num_peds_waiting()
        uniform = sim.button_tr.get_next()

        # calculate the probability button will be pushed
        if num_waiting == 0:
            thresh = 15.0 / 16.0
        else:
            thresh = 1.0 / (num_waiting + 1)

        if uniform < thresh:
            print("[EVENT] pushing button")
            sim.push_button()

    # create impatient event if ped might be held up for >1min
    elif sim.road.state == StoplightState.GREEN \
      or sim.road.state == StoplightState.GREEN_EXPIRED:
        print("[EVENT] creating ped_impatient event")
        impatient_event = (sim.time + 60, ped_impatient, (ped_id, ))
        sim.q.put(impatient_event)


def ped_impatient(sim, ped_id):
    print("[EVENT] ped_impatient")
    # check if the signal has changed in the last minute
    # if so, ignore impatient event
    if sim.road.last_walk + 60 < sim.time:
        print("[EVENT] ped_impatient: cancelled")
        return

    # push the button
    sim.push_button()


def green_expires(sim):
    print("[EVENT] green_expires")
    # update state based on if walk button has been pushed
    # if not pushed, just move to expired state
    if sim.road.state == StoplightState.GREEN:
        sim.road.update_state(StoplightState.GREEN_EXPIRED, sim.time)

    # if button was already pushed, trigger yellow light
    elif sim.road.state == StoplightState.GREEN_WAITING:
        sim.road.update_state(StoplightState.YELLOW, sim.time)
        # add yellow_expires event
        next_expire = (sim.time + sim.road.t_yellow, yellow_expires, ())
        sim.q.put(next_expire)


def yellow_expires(sim):
    print("[EVENT] yellow_expires")
    # update state to RED; this is also WALK
    sim.road.update_state(StoplightState.RED, sim.time)

    #TODO: crosswalk logic

    # delay vehicles that would be in the crosswalk


def red_expires(sim):
    print("[EVENT] red_expires")
    # update state to GREEN
    sim.road.update_state(StoplightState.GREEN, sim.time)

    # clean up crosswalk? what needs to be done here?
    # some pedestrians will push button (case c in assignment)


def auto_exit(sim, auto_id):
    # store total travel time

    # remove auto from simulation

    print("[EVENT] auto_exit")

def ped_exit(sim, ped_id):
    # store total travel time

    # remove ped from simulation

    print("[EVENT] ped_exit")
