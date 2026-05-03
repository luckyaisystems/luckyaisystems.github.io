def evaluate_rung(rung, inputs, state):
    op = rung["op"]

    # Boolean logic
    if op == "AND":
        return all(inputs.get(i, False) for i in rung["in"])

    if op == "OR":
        return any(inputs.get(i, False) for i in rung["in"])

    if op == "NOT":
        return not inputs.get(rung["in"][0], False)

    # Latching logic
    if op == "SET":
        if all(inputs.get(i, False) for i in rung["in"]):
            state.memory[rung["out"]] = True
        return state.memory.get(rung["out"], False)

    if op == "RESET":
        if all(inputs.get(i, False) for i in rung["in"]):
            state.memory[rung["out"]] = False
        return state.memory.get(rung["out"], False)

    # Timers, counters, etc. will go here later
