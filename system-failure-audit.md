---
title: System Failure Audit
---

# System Failure Audit

A deterministic logic engine for classifying failure modes across input, operator, and execution layers — inspired by PLC safety interlocks and AI-assisted decision systems.

[View the full project on GitHub](https://github.com/luckyaisystems/system-failure-audit)

![System Failure Audit Diagram](https://raw.githubusercontent.com/luckyaisystems/system-failure-audit/main/Screenshot%202026-05-03%204.01.12%20PM.png
)

## Failure Mode Classification Table

| Layer           | Failure Type     | Description                                                |
|-----------------|------------------|------------------------------------------------------------|
| Input Layer     | Model Error      | Bad, missing, corrupted, or out-of-range data             |
| Decision Layer  | Operator Error   | Bias, emotion, logic violation, or unsafe decision path   |
| Execution Layer | Execution Decay  | Timing failures, actuator breakdown, or incomplete execution |

This mirrors how industrial safety systems isolate failures across sensing, logic, and actuation.

## Code Overview

The [`failure_audit.py`](https://github.com/luckyaisystems/system-failure-audit/blob/main/failure_audit.py) script implements a deterministic 3-layer failure classifier:

- **Input Layer (Model Error)** — Detects bad or corrupted data  
- **Decision Layer (Operator Error)** — Detects bias, emotion, or logic violations  
- **Execution Layer (Execution Decay)** — Detects timing failures, actuator breakdowns, or incomplete execution  

## Example Output

```text
Input Layer: PASS
Decision Layer: FAIL — Operator logic violation detected
Execution Layer: PASS

Overall System Status: FAILURE — Operator Error
```

This demonstrates how the classifier isolates the failure point in a system.
## Deterministic Rules (Core Logic)

### Input Layer FAIL if:
- data is None
- data is outside predefined bounds
- checksum or validation fails

### Decision Layer FAIL if:
- rule violation detected
- conflicting decisions generated
- undefined or unsafe state reached

### Execution Layer FAIL if:
- timeout exceeded
- actuator response incomplete
- final state does not match expected output

## Example Python Implementation

```python
def audit_system(data, decision, execution):
    input_ok = data is not None and 0 <= data <= 100
    decision_ok = decision in ["ALLOW", "DENY"]
    execution_ok = execution == "COMPLETED"

    if not input_ok:
        return "FAILURE — Model Error"
    if not decision_ok:
        return "FAILURE — Operator Error"
    if not execution_ok:
        return "FAILURE — Execution Decay"

    return "PASS"
```
