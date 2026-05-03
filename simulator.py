from logic_engine import evaluate_rung
from plc_state import PLCState
from rungs import rungs

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
