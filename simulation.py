# Simulation.py
# Eric Olson
# Computer Simulation, Fall 2017

# python imports
import configparser
import math
from queue import PriorityQueue

# local imports
import event
import road
from trace_reader import TraceReader


class Simulation:

    #
    # setup functions
    #
    def __init__(self, n, config_filename, auto_trace, ped_trace, button_trace):
        # N is the number of vehicles and pedestrians to create
        self.n = n

        # initialize time
        self.time = 0

        # note on priority queue:
        # each entry is of the form (time, function, params).
        self.q = PriorityQueue()

        # set up trace readers
        self.auto_tr = TraceReader(auto_trace)
        self.ped_tr = TraceReader(ped_trace)
        self.button_tr = TraceReader(button_trace)

        # read config variables
        self.read_config_variables(config_filename)

        # create a road
        self.road = road.Road(0, self.t_red, self.t_yellow, self.t_green)

        # initialize welford variables
        self.avg_auto_delay = 0
        self.auto_i = 0
        self.auto_delay_variance = 0
        self.avg_ped_delay = 0
        self.ped_i = 0

        # set up simulation state
        self.setup_sim()

    def read_config_variables(self, config_filename):
        # read in variables from input file
        config = configparser.ConfigParser()
        config.read(config_filename)
        # extract sim_params section from config file
        sim_params = config['sim_params']
        self.block_width     = sim_params.getint('block_width')
        self.crosswalk_width = sim_params.getint('crosswalk_width')
        self.street_width    = sim_params.getint('street_width')
        self.t_red           = sim_params.getint('t_red')
        self.t_yellow        = sim_params.getint('t_yellow')
        self.t_green         = sim_params.getint('t_green')
        self.ped_rate        = sim_params.getint('ped_rate')
        self.ped_mu          = 60 / self.ped_rate
        self.auto_rate       = sim_params.getint('auto_rate')
        self.auto_mu         = 60 / self.auto_rate
        self.auto_length     = sim_params.getint('auto_length')
        self.auto_speed_min  = sim_params.getint('auto_speed_min')
        self.auto_speed_max  = sim_params.getint('auto_speed_max')
        self.auto_accel      = sim_params.getint('auto_accel')
        self.ped_speed_min   = sim_params.getfloat('ped_speed_min')
        self.ped_speed_max   = sim_params.getfloat('ped_speed_max')

        # compute road length (i.e. total auto travel distance)
        self.road_length = 7 * self.block_width + 6 * self.street_width
        # compute distance to crosswalk
        self.distance_to_crosswalk = 7/2 * self.block_width + 3 * self.street_width - self.crosswalk_width / 2

    def setup_sim(self):
        # generate initial arrival times
        uniform = self.auto_tr.get_next()
        t1 = -1 * self.auto_mu * math.log(uniform)
        uniform = self.auto_tr.get_next()
        t2 = -1 * self.auto_mu * math.log(uniform)
        uniform = self.ped_tr.get_next()
        t3 = -1 * self.ped_mu * math.log(uniform)
        uniform = self.ped_tr.get_next()
        t4 = -1 * self.ped_mu * math.log(uniform)

        # create arrivals and add to queue
        arr1 = (t1, event.auto_arrival, (0, ))
        arr2 = (t2, event.auto_arrival, (1, ))
        arr3 = (t3, event.ped_arrival, (0, ))
        arr4 = (t4, event.ped_arrival, (1, ))
        self.q.put(arr1)
        self.q.put(arr2)
        self.q.put(arr3)
        self.q.put(arr4)

    #
    # welford functions
    #
    def auto_delay(self, delay):
        # update avg auto delay and sample variance based on welford equation
        print("[SIM]  updating auto delay & variance")
        self.auto_i += 1
        auto_i = self.auto_i
        auto_delay_variance = self.auto_delay_variance
        avg_auto_delay = self.avg_auto_delay

        self.auto_delay_variance = auto_delay_variance + ( (auto_i-1) / auto_i ) * ( (delay - avg_auto_delay) ** 2)
        self.avg_auto_delay = avg_auto_delay + (1 / auto_i) * (delay - avg_auto_delay)

    def ped_delay(self, delay):
        # update avg ped delay based on welford equation
        print("[SIM]  updating ped delay")
        self.ped_i += 1
        self.avg_ped_delay = self.avg_ped_delay + (1 / self.ped_i) * (delay - self.avg_ped_delay)


    #
    # helper functions
    #
    def push_button(self):
        print("[SIM]  button pushed")

        # tell road to push button, save state change
        state_change = self.road.push_button(self.time)

        # add timer expiration event if light changed to yellow
        if state_change == road.StoplightState.YELLOW:
            print("[SIM]  adding yellow_expires event")
            next_expire = (self.time + self.road.t_yellow, event.yellow_expires, ())
            self.q.put(next_expire)

    #
    # pRNG functions
    #
    def auto_speed_prng(self):
        # get a Uniform(0,1) value
        x = self.auto_tr.get_next()
        # convert to Uniform(a,b)
        a = self.auto_speed_min
        b = self.auto_speed_max

        return a + (b - a) * x

    def ped_speed_prng(self):
        # get a Uniform(0,1) value
        x = self.ped_tr.get_next()
        # convert to Uniform(a,b)
        a = self.ped_speed_min
        b = self.ped_speed_max

        return a + (b - a) * x

    def button_prng(self):
        # no conversion needed for button. Uniform(0,1) is fine
        return self.button_tr.get_next()


    #
    # SIM execution functions
    #
    def run_sim(self):
        print ("[SIM]  STARTING SIM...")
        while not self.q.empty():
            # pop the next event from queue
            next_event = self.q.get()
            print ("[SIM]  next event: {}".format(next_event))
            # unpack the event tuple
            # event tuple format: (time, function, params)
            self.time = next_event[0]
            eventhandler = next_event[1]
            params = next_event[2]
            # add simulation as first param
            params = (self,) + params

            # call the event handler function
            eventhandler(*params)
            print ("[SIM]  done with event\n")
        self.sim_complete()
        return

    def sim_complete(self):
        print ("\n[SIM]  SIM COMPLETE")
        variance = self.auto_delay_variance / self.auto_i
        print ("auto i: {}, ped i: {}".format(self.auto_i, self.ped_i))
        print ("OUTPUT auto delay {}".format(self.avg_auto_delay))
        print ("OUTPUT auto variance {}".format(variance))
        print ("OUTPUT ped delay {}".format(self.avg_ped_delay))
        return


