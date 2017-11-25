# trace_reader.py
# Author: Eric Olson
#
# Read trace files and output them like random.random()

class TraceReader:
    def __init__(self, filename):
        self.infile = open(filename)
        self.it = iter(self)

    def __iter__(self):
        for line in self.infile:
            yield line

    def get_next(self):
        val = next(self.it)
        return float(val.rstrip())

    def close(self):
        close(infile)

