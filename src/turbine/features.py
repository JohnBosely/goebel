"""
Feature engineering for C-MAPSS turbine RUL data.

TODO:
- load_cmapss(path) -> DataFrame with columns: unit, cycle, op_setting_1..3, sensor_1..21
- add_rolling_features(df, window=5) -> rolling mean/std/rate-of-change per unit, per sensor
- add_rul_labels(df) -> RUL = max_cycle_for_unit - current_cycle
"""

import pandas as pd


def load_cmapss(path: str) -> pd.DataFrame:
    raise NotImplementedError


def add_rolling_features(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    raise NotImplementedError


def add_rul_labels(df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
