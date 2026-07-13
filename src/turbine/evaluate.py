"""
Evaluation for turbine RUL: RMSE + PHM08 asymmetric scoring function.

PHM08 score penalizes late predictions more than early ones:
    if d < 0:  score = exp(-d/13) - 1   (early prediction, small penalty)
    if d >= 0: score = exp(d/10) - 1    (late prediction, big penalty)
    where d = predicted_RUL - true_RUL
"""
import numpy as np


def rmse(y_true, y_pred) -> float:
    return float(np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2)))


def phm08_score(y_true, y_pred) -> float:
    d = np.array(y_pred) - np.array(y_true)
    scores = np.where(d < 0, np.exp(-d / 13) - 1, np.exp(d / 10) - 1)
    return float(np.sum(scores))
