"""
FastAPI backend serving all three Goebel models via separate endpoints.

TODO endpoints:
  POST /predict/turbine    -> RUL prediction + SHAP "why"
  POST /predict/bearing    -> fault classification + confidence + SHAP "why"
  POST /predict/hydraulic  -> 4 component health scores + SHAP "why"
  GET  /benchmarks         -> published benchmark comparison data
  GET  /health             -> simple liveness check
"""
from fastapi import FastAPI

app = FastAPI(title="Goebel — Multi-Asset Predictive Maintenance Platform")


@app.get("/health")
def health():
    return {"status": "ok"}


# @app.post("/predict/turbine")
# def predict_turbine(payload: ...):
#     raise NotImplementedError

# @app.post("/predict/bearing")
# def predict_bearing(payload: ...):
#     raise NotImplementedError

# @app.post("/predict/hydraulic")
# def predict_hydraulic(payload: ...):
#     raise NotImplementedError
