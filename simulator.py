from logic_engine import evaluate_rung

def scan_cycle(inputs):
    """
    One PLC scan cycle:
    1. Read inputs
    2. Evaluate logic
    3. Update outputs
    """
    output = evaluate_rung(inputs)
    return {"Y1": output}


if __name__ == "__main__":
    # Example test
    test_inputs = {"X1": True, "X2": False}
    print(scan_cycle(test_inputs))

