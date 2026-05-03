from logic_engine import evaluate_rung
from plc_state import PLCState
from rungs import rungs   # if you created rungs.py

def scan_cycle(state, rungs):
    """
    PLC scan cycle with persistent memory image.
    """

    # Use the existing output image (PLC behavior)
    outputs = state.outputs

    for rung in rungs:
        result = evaluate_rung(rung, state.inputs)
        outputs[rung["output"]] = result

    # Write back to state
    state.outputs = outputs
    return state


if __name__ == "__main__":
    state = PLCState()
    state.inputs = {"X1": True, "X2": False}

    updated_state = scan_cycle(state, rungs)
    print(updated_state.outputs)
