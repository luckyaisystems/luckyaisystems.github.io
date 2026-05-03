from logic_engine import evaluate_rung
from plc_state import PLCState
from rungs import rungs

def scan_cycle(state, rungs):
    """
    Deterministic PLC scan cycle:
    - read stable input image
    - compute next output image
    - commit at end of scan
    """

    next_outputs = state.outputs.copy()  # snapshot

    for rung in rungs:
        result = evaluate_rung(rung, state.inputs, state)
        next_outputs[rung["output"]] = result

    # atomic commit
    state.outputs = next_outputs
    return state
