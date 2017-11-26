# Simulation.py
# Eric Olson
# Computer Simulation, Fall 2017

import configparser
from queue import PriorityQueue
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
        # each entry is of the form (time, id, handler_function).
        # if ID is None, handler function doesn't take an ID (like green_expires)
        self.q = PriorityQueue()

        # set up trace readers
        self.auto_tr = TraceReader(auto_trace)
        self.ped_tr = TraceReader(ped_trace)
        self.button_tr = TraceReader(button_trace)

        # set up simulation state
        setup_sim()

        # run simulation
        run_sim()

    def read_config_variables(self):
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
        self.auto_rate       = sim_params.getint('auto_rate')
        self.auto_length     = sim_params.getint('auto_length')
        self.auto_speed_min  = sim_params.getint('auto_speed_min')
        self.auto_speed_max  = sim_params.getint('auto_speed_max')
        self.auto_accel      = sim_params.getint('auto_accel')
        self.ped_speed_min   = sim_params.getfloat('ped_speed_min')
        self.ped_speed_max   = sim_params.getfloat('ped_speed_max')

    def setup_sim(self):
        # set up the initial state of the simulation
        return

    #
    # pRNG functions
    #
    def auto_speed_prng():
        # TODO: read trace file
        return 26.8
    def ped_speed_prng():
        # TODO: read trace file
        return 3.0
    def button_prng():
        # TODO: read trace file
        return 0.5

    #
    # SIM execution functions
    #
    def run_sim(self):
        print "[SIM]  STARTING SIM..."
        while not q.empty():
            # pop the next event from queue
            next_event = q.get()
            print "[SIM]  next event: {}".format(next_event)
            # unpack the event tuple
            # event tuple format: (time, function, params)
            self.time = next_event[0]
            eventhandler = next_event[1]
            params = next_event[2]

            # call the event handler function
            eventhandler(*params)
            print "[SIM]  done with event"

        return

    def sim_complete(self):
        print "[SIM]  SIM COMPLETE"
        return


