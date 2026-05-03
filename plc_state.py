class PLCState:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.memory = {}     # internal bits (M registers)
        self.timers = {}
        self.counters = {}

