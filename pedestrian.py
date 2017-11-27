
class Pedestrian:
    def __init__(self, num, prng, current_time):
        self.num = num

        self.arrival = current_time

        self.speed = prng()

        print ("[PED]  created with id: {}, speed: {}".format(self.num, self.speed))

    def calc_travel_time(self, distance):
        # calculate expected travel time

        # return calculated time
        return

    def calc_crosswalk_time(self, dist_to_crosswalk):
        # calculate when ped will arrive at crosswalk

        # return expected time
        return

    def light_red(self, current_time, t_red):
        # when light turns red, ped can likely cross

        # return delay time? if crossed?
        return

