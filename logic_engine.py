def evaluate_rung(inputs):
    """
    Minimal deterministic rung:
    X1 AND X2 → Y1
    """
    return inputs.get("X1", False) and inputs.get("X2", False)

