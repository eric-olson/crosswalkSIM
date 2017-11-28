
class Auto:
    def __init__(self, num, prng, current_time, accel, length, delayed=False):
        # set id num
        self.num = num

        # set arrival time to current time
        self.arrival = current_time

        # use prng to set speed
        self.speed_mph = prng()
        # speed is in MPH, convert to ft/sec
        self.speed = self.speed_mph * 5280.0 / 60.0 / 60.0

        # store delayed state
        self.delayed = delayed

        # store acceleration
        self.accel = accel

        # store length
        self.length = length

        # print debug message
        print ("[AUTO] created with id: {}, speed: {}, " \
               "accel: {}, length: {} delayed: {}".format(self.num,
                                                          self.speed,
                                                          self.accel,
                                                          self.length,
                                                          self.delayed))

    def calc_travel_time(self, distance):
        # calculate expected travel time
        self.travel_time = self.time_from_dist(distance)
        self.travel_dist = distance
        print("[AUTO] calculated travel_time = {} s".format(self.travel_time))

        # return calculated time
        return self.travel_time


    def calc_crosswalk_time(self, dist_to_crosswalk, crosswalk_width, time):
        # calculate entry & exit times
        self.dist_to_crosswalk = dist_to_crosswalk
        self.enter_crosswalk = time + self.time_from_dist(dist_to_crosswalk)
        self.exit_crosswalk = self.enter_crosswalk + self.time_from_dist(crosswalk_width + self.length)
        print("[AUTO] calculated enter_crosswalk = {} s".format(self.enter_crosswalk))
        print("[AUTO] calculated exit_crosswalk = {} s".format(self.exit_crosswalk))

        # return times because why not
        return (self.enter_crosswalk, self.exit_crosswalk)

    def time_from_dist(self, distance):
        # helper to calculate travel times
        return distance / self.speed


    def red_light(self, current_time, t_red):
        # if time is within crosswalk window, delay
        red_end = current_time + t_red
        # check if auto will NOT be delayed. if not, return zero delay
        if self.exit_crosswalk < current_time or self.enter_crosswalk > red_end:
            # auto could still enter crosswalk, no delay can be proven yet
            return None

        print("[AUTO] delaying auto {}".format(self.num))
        delayed = True
        self.calc_delay(red_end)

        return self.delay

    def calc_delay(self, red_end):
        # add time spent accelerating & decelerating
        braking_distance = self.speed ** 2 / (2 * self.accel)
        braking_time = self.speed / self.accel
        # recalculate initial travel time, excluding braking distance
        self.initial_travel_time = self.travel_time
        self.calc_travel_time(self.travel_dist - braking_distance)
        # add braking time to travel time
        self.travel_time += 2 * braking_time

        # calculate new crosswalk arrival time
        brake_start = (self.dist_to_crosswalk - braking_distance) / self.speed
        halt_time = self.arrival + brake_start + braking_time

        wait_time = red_end - halt_time

        self.travel_time += wait_time

        # calculate delay
        self.delay = self.travel_time - self.initial_travel_time

        print("[AUTO] calculated delay = {} s".format(self.delay))

