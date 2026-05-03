from logic_engine import evaluate_rung
from plc_state import PLCState
from rungs import rungs


def scan_cycle(state, rungs):
    next_outputs = state.outputs.copy()

    for rung in rungs:
        result = evaluate_rung(rung, state.inputs)

        if result is None:
            continue

        if result["type"] == "COIL":
            next_outputs[rung["out"]] = result["value"]

        elif result["type"] == "SET":
            state.memory[result["target"]] = True

        elif result["type"] == "RESET":
            state.memory[result["target"]] = False

    state.outputs = next_outputs
    return state

