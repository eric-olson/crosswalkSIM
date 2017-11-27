
class Pedestrian:
    def __init__(self, num, prng, current_time):
        self.num = num

        self.arrival = current_time

        self.speed = prng()

        self.crossed_street = False

        print ("[PED]  created with id: {}, speed: {}".format(self.num, self.speed))

    def calc_travel_time(self, travel_distance):
        # calculate expected travel time

        # return calculated travel time (not clock time)
        return

    def calc_crosswalk_time(self, dist_to_crosswalk):
        # calculate when ped will arrive at crosswalk

        # return expected arrival time
        return

    def calc_cross_time(self, street_width):
        # calculate time taken to cross street
        return

    def time_from_dist(self, distance):
        # helper to calculate travel times based on distance and speed
        return


    def light_red(self, current_time, t_red):
        # when light turns red, ped can likely cross

        # return delay time? if crossed?
        return

