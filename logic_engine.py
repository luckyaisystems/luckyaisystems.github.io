# logic_engine.py

def evaluate_rung(rung, inputs):
    if rung["type"] == "AND":
        return all(inputs.get(i, False) for i in rung["inputs"])
    elif rung["type"] == "OR":
        return any(inputs.get(i, False) for i in rung["inputs"])
    elif rung["type"] == "NOT":
        return not inputs.get(rung["inputs"][0], False)
