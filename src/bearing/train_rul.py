"""
Run-to-failure RUL regression on IMS bearing dataset,
once a fault has been detected by train_classifier.py.

Also home for the cross-dataset generalization test:
train on CWRU, evaluate on IMS (and vice versa), report honestly.
"""

def train():
    raise NotImplementedError


def cross_dataset_eval():
    """Train on one dataset, test on the other. Report the accuracy drop honestly."""
    raise NotImplementedError


if __name__ == "__main__":
    train()
