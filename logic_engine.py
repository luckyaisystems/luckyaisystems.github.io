def evaluate_rung(rung, inputs, state, dt):
    op = rung["op"]

    if op == "AND":
        return {"type": "COIL", "value": all(inputs.get(i, False) for i in rung["in"])}

    if op == "OR":
        return {"type": "COIL", "value": any(inputs.get(i, False) for i in rung["in"])}

    if op == "NOT":
        return {"type": "COIL", "value": not inputs.get(rung["in"][0], False)}

    if op == "SET":
        condition = all(inputs.get(i, False) for i in rung["in"])
        if condition:
            return {"type": "SET", "target": rung["out"]}
        return None

    if op == "RESET":
        condition = all(inputs.get(i, False) for i in rung["in"])
        if condition:
            return {"type": "RESET", "target": rung["out"]}
        return None

    if op == "TON":
        timer_id = rung["out"]
        preset = rung["params"]["preset"]

        if timer_id not in state.timers:
            state.timers[timer_id] = {"acc": 0, "done": False, "preset": preset}

        timer = state.timers[timer_id]
        condition = all(inputs.get(i, False) for i in rung["in"])

        if condition:
            timer["acc"] += dt
            if timer["acc"] >= timer["preset"]:
                timer["done"] = True
        else:
            timer["acc"] = 0
            timer["done"] = False

        return {"type": "TIMER", "target": timer_id}

