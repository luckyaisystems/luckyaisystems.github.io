# rungs.py or top of simulator.py

rungs = [
    {"type": "AND", "inputs": ["X1", "X2"], "output": "Y1"}
]
# simulator.py

from logic_engine import evaluate_rung
from rungs import rungs   # if you put rungs in a separate file

def scan_cycle(inputs):
    outputs = {}

    for rung in rungs:
        result = evaluate_rung(rung, inputs)
        outputs[rung["output"]] = result

    return outputs
