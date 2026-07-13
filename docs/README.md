# Goebel — Multi-Asset Predictive Maintenance Platform

A system that ingests sensor telemetry from three industrial asset types
(turbine engines, bearings, hydraulic systems), predicts Remaining Useful
Life and failure probability, classifies likely fault type, and explains
which sensors drive each prediction.

## Sub-systems
1. **Turbine RUL** — C-MAPSS, regression (XGBoost/RF), evaluated on RMSE + PHM08 scoring
2. **Bearing faults** — CWRU + IMS, FFT features, fault classification + RUL, cross-dataset generalization test
3. **Hydraulic health** — UCI Hydraulic, 4-component health scoring

## Status
- [ ] Turbine RUL
- [ ] Bearing fault classification
- [ ] Bearing RUL + cross-dataset test
- [ ] Hydraulic health scoring
- [ ] SHAP explainability (all 3)
- [ ] FastAPI backend
- [ ] Streamlit dashboard
- [ ] Docker deployment
- [ ] Benchmark comparison + honest limitations write-up

## Quickstart
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload          # backend
streamlit run dashboard/app.py         # dashboard (separate terminal)
```

## Architecture
(diagram TODO — add once pipeline is working end to end)

## Benchmarks
See `src/shared/benchmarks.py` for published numbers being compared against.

## Limitations
(fill in honestly as you go — e.g. static datasets, not live streaming)
