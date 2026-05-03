from logic_engine import evaluate_rung
from plc_state import PLCState
from rungs import rungs
import time


def scan_cycle(state, rungs, dt):
    next_outputs = state.outputs.copy()

    for rung in rungs:
        result = evaluate_rung(rung, state.inputs, state, dt)

        if result is None:
            continue

        if result["type"] == "COIL":
            next_outputs[rung["out"]] = result["value"]

        elif result["type"] == "SET":
            state.memory[result["target"]] = True

        elif result["type"] == "RESET":
            state.memory[result["target"]] = False

    # expose timer done bits as readable inputs (e.g., "T1")
    for name, timer in state.timers.items():
        state.inputs[name] = timer["done"]

    state.outputs = next_outputs
    return state
if __name__ == "__main__":
    state = PLCState()
    state.inputs = {"X1": False}

    SCAN_TIME = 0.01  # 10 ms

    t = 0  # simple time accumulator

    while True:
        # simulate input change at runtime
        if t == 100:   # after 100 scans (~1 second)
            state.inputs["X1"] = True

        if t == 200:   # after 200 scans (~2 seconds)
            state.inputs["X1"] = False

        state = scan_cycle(state, rungs, dt=SCAN_TIME * 1000)

        print("Inputs:", state.inputs)
        print("Outputs:", state.outputs)
        print("Timers:", state.timers)
        print("---")

        time.sleep(SCAN_TIME)
        t += 1


