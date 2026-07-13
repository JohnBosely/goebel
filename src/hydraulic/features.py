"""
Feature engineering for UCI Hydraulic dataset.
Same rolling-window approach as turbine (Sub-System 1).

TODO:
- load_hydraulic(path) -> pressure/flow/temp sensor readings per cycle
- add_rolling_features(df, window=5)
- align with the 4 component degradation labels: cooler, valve, pump, accumulator
"""

def load_hydraulic(path: str):
    raise NotImplementedError


def add_rolling_features(df, window: int = 5):
    raise NotImplementedError
