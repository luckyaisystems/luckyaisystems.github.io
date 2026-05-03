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

        elif result["type"] == "TIMER":
            pass  # timer state already updated in state.timers

    state.outputs = next_outputs
    return state


# ⭐⭐⭐ THIS IS THE MAIN LOOP — PUT IT AT THE BOTTOM ⭐⭐⭐
if __name__ == "__main__":
    state = PLCState()

    # Example input
    state.inputs = {"X1": False}

    SCAN_TIME = 0.01  # 10ms scan time

    while True:
        state = scan_cycle(state, rungs, dt=SCAN_TIME * 1000)  # dt in ms

        print("Outputs:", state.outputs)
        print("Memory:", state.memory)
        print("Timers:", state.timers)
        print("---")

        time.sleep(SCAN_TIME)

