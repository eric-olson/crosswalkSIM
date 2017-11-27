
class Pedestrian:
    def __init__(self, num, prng, current_time):
        self.num = num

        self.arrival = current_time

        self.speed = prng()

        self.crossed_street = False

        print ("[PED]  created with id: {}, speed: {}".format(self.num, self.speed))

    def calc_travel_time(self, travel_distance):
        # calculate expected travel time
        travel_time = self.time_from_dist(travel_distance)
        self.travel_time = travel_time
        print("[PED]  calculated travel_time = {} s".format(travel_time))

        # return calculated travel time (not clock time) for welford
        return travel_time

    def calc_crosswalk_time(self, dist_to_crosswalk):
        # calculate when ped will arrive at crosswalk
        crosswalk_time = self.time_from_dist(dist_to_crosswalk)
        self.crosswalk_time = crosswalk_time
        print("[PED]  calculated crosswalk_time = {} s".format(crosswalk_time))

        # return expected arrival time for event creation
        return crosswalk_time

    def calc_cross_time(self, street_width):
        # calculate time taken to cross street
        cross_time = self.time_from_dist(street_width)
        self.cross_time = cross_time
        print("[PED]  calculated cross_time = {} s".format(cross_time))

        return cross_time

    def time_from_dist(self, distance):
        # helper to calculate travel times based on distance and speed
        return distance / self.speed


    def light_red(self, current_time, t_red):
        # when light turns red, ped can likely cross

        # return delay time? if crossed?
        return

