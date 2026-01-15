import os
try:
    import joblib
except Exception:
    joblib = None

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def load_model():
    if joblib is None:
        return None
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def predict(features, model=None):
    """Placeholder predict: expects features as list-like numeric vector or dict.
    """
    if model is None:
        model = load_model()
    if model is None:
        return 0.0
    # transform features if needed
    return float(model.predict_proba([features])[0][1])
