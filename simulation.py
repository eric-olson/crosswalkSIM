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
    def __init__(self, config_filename, auto_trace, ped_trace, button_trace):
        # initialize time and queue
        self.time = 0
        self.q = PriorityQueue()

        # set up trace readers
        self.auto_tr = TraceReader(auto_trace)
        self.ped_tr = TraceReader(ped_trace)
        self.button_tr = TraceReader(button_trace)

    def read_config_variables():
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

    def setup_sim():

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
    def run_sim():
        print "STARTING SIM"
        return

    def sim_complete():
        print "SIM COMPLETE"
        return


