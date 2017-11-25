
class Auto:
    def __init__(self, prng, current_time):
        # set arrival time to current time
        self.arrival = current_time
        # store the pRNG for auto arrivals & speeds
        self.prng = prng
        self.speed = prng()



