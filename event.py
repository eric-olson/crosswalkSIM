
from enum import Enum

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

def auto_arrival(auto_id, q):
    # add new auto to queue (what about direction?)

    # compute expected exit time

    # precompute time at crosswalk

    # create next arrival event

    print("auto_arrival")

def ped_arrival(ped_id, q):
    # calculate time to arrive at button & create event

    # precompute total travel time, minus delay

    print("ped_arrival")

def ped_at_button(ped_id, q):
    # determine if pedestrian will push button

    # create impatient event

    print("ped_at_button")

def ped_impatient(ped_id, q):
    # check if ped has crossed the street yet

    # push the button

    print("ped_impatient")

def green_expires(q):
    # update state based on if walk button has been pushed

    print("green_expires")

def yellow_expires(q):
    # update state

    # delay vehicles that would be in the crosswalk

    print("yellow_expires")

def red_expires(q):
    # update state

    # clean up crosswalk? what needs to be done here?

    print("red_expires")

def auto_exit(auto_id, q):
    # store total travel time

    # remove auto from simulation

    print("auto_exit")

def ped_exit(ped_id, q):
    # store total travel time

    # remove ped from simulation

    print("ped_exit")
