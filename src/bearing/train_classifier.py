"""
Fault-type classifier (healthy / inner race / outer race / ball fault) on CWRU.
Benchmark to beat: published CWRU accuracy is typically 95-99%+.

TODO:
- build feature matrix from fft_features() across all CWRU samples
- train RandomForest classifier
- save to models/bearing/
"""

def train():
    raise NotImplementedError


if __name__ == "__main__":
    train()
