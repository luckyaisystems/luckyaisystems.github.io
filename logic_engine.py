def evaluate_rung(rung, inputs):
    op = rung["op"]

    if op == "AND":
        return {"type": "COIL", "value": all(inputs.get(i, False) for i in rung["in"])}

    if op == "OR":
        return {"type": "COIL", "value": any(inputs.get(i, False) for i in rung["in"])}

    if op == "NOT":
        return {"type": "COIL", "value": not inputs.get(rung["in"][0], False)}

    if op == "SET":
        if all(inputs.get(i, False) for i in rung["in"]):
            return {"type": "SET", "target": rung["out"]}
        return None

    if op == "RESET":
        if all(inputs.get(i, False) for i in rung["in"]):
            return {"type": "RESET", "target": rung["out"]}
        return None

