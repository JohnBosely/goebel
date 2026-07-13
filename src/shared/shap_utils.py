"""
Shared SHAP explainability helpers, used across all three sub-systems.
Same library you already used in NIDS.

TODO:
- get_explainer(model) -> shap.Explainer, auto-picks TreeExplainer for XGBoost/RF
- top_features(explainer, X_row, n=5) -> list of (feature_name, shap_value)
  used to generate the plain-English "why" string per prediction
- shap_bar_chart(explainer, X_row) -> for the Streamlit explainability panel
"""

def get_explainer(model):
    raise NotImplementedError


def top_features(explainer, x_row, n: int = 5):
    raise NotImplementedError
