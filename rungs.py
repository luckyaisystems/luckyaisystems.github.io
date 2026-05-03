{
    "op": "AND" | "OR" | "NOT" | "SET" | "RESET" | "TON" | ...,
    "in": ["X1", "X2"],      # inputs (list or single)
    "out": "Y1",             # output coil or memory bit
    "params": {...}          # optional (timers, counters)
}
rungs = [
    # Seal-in rung
    {"op": "AND", "in": ["X1", "Y1"], "out": "Y1"}
]
