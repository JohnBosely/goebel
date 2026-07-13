"""
Four separate health-scoring models (or one multi-output model):
cooler, valve, pump, accumulator.

Decide: binary (healthy/degraded) vs continuous (0-100%) —
check UCI label granularity before committing (see PART 8 of project doc).

TODO:
- train_component(name, df) -> model per component
- or train_multioutput(df) -> single multi-output model
- save to models/hydraulic/
"""

def train():
    raise NotImplementedError


if __name__ == "__main__":
    train()
