"""
Streamlit dashboard — three tabs, one per asset type, each with an
explainability panel (SHAP bar chart) and a benchmark comparison page.

TODO:
- tab 1: Turbine  — live RUL countdown per engine, sensor trend graph
- tab 2: Bearing  — fault classification, confidence, estimated remaining life
- tab 3: Hydraulic — 4 component health gauges
- shared: benchmark comparison page, cross-dataset generalization report
"""
import streamlit as st

st.set_page_config(page_title="Goebel", layout="wide")
st.title("Goebel — Multi-Asset Predictive Maintenance Platform")

tab1, tab2, tab3 = st.tabs(["Turbine", "Bearing", "Hydraulic"])

with tab1:
    st.write("TODO: RUL countdown + sensor trends")

with tab2:
    st.write("TODO: fault classification + RUL")

with tab3:
    st.write("TODO: 4 component health gauges")
