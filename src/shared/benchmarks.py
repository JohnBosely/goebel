"""
Published research benchmarks to compare Goebel's results against.
Fill in as you find sources — keep citations for the README benchmark table.
"""

BENCHMARKS = {
    "turbine": {
        "dataset": "C-MAPSS FD001",
        "metric": "RMSE",
        "published_range": (15, 25),  # cycles, varies by sub-dataset FD001-FD004
        "source": "TODO: cite specific paper(s) you compare against",
    },
    "bearing": {
        "dataset": "CWRU",
        "metric": "classification accuracy",
        "published_range": (0.95, 0.99),
        "source": "TODO: cite specific paper(s) you compare against",
    },
    "hydraulic": {
        "dataset": "UCI Hydraulic",
        "metric": "TBD — depends on binary vs continuous scoring decision",
        "published_range": None,
        "source": "TODO",
    },
}
