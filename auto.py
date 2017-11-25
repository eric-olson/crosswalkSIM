
class Auto:
    def __init__(self, num, prng, current_time, accel, delayed=False):
        # set id num
        self.num = num

        # set arrival time to current time
        self.arrival = current_time

        # use prng to set speed
        self.speed = prng()

        # store delayed state
        self.delayed = delayed

        # store acceleration
        self.accel = accel

        # print debug message
        print "[AUTO] created with id: {}, speed: {}".format(self.num, self.speed)

    def calc_travel_time(self, distance):
        # calculate expected travel time

        # return calculated time
        return


    def calc_crosswalk_time(self, dist_to_crosswalk, crosswalk_width):
        # calculate entry & exit times

        # return times because why not
        return

    def light_red(self, current_time, t_red):
        # if time is within crosswalk window, delay

        # return something for welford?
        return

