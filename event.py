
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

def auto_arrival():
    # add new auto to queue (what about direction?)

    # compute expected exit time

    # precompute time at crosswalk

    # create next arrival event

    print("auto_arrival")

def ped_arrival():
    print("ped_arrival")

def ped_at_button():
    print("ped_at_button")

def ped_impatient():
    print("ped_impatient")

def green_expires():
    print("green_expires")

def yellow_expires():
    print("yellow_expires")

def red_expires():
    print("red_expires")

def auto_exit():
    print("auto_exit")

def ped_exit():
    print("ped_exit")
