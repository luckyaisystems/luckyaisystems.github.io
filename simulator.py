from logic_engine import evaluate_rung
from rungs import rungs   # or define rungs above

def scan_cycle(inputs):
    outputs = {}

    for rung in rungs:
        result = evaluate_rung(rung, inputs)
        outputs[rung["output"]] = result

    return outputs


if __name__ == "__main__":
    test_inputs = {"X1": True, "X2": False}
    print(scan_cycle(test_inputs))
