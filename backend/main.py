from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

from multilang_analyzer import extract_features
from model import predict, load_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from frontend directory
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

_model = load_model()


@app.get("/")
def root():
    """Serve the main HTML file"""
    return FileResponse(os.path.join(frontend_dir, "index.html"))


class ReviewRequest(BaseModel):
    code: str
    language: str = "python"  # Default to Python


@app.post("/review")
def review(req: ReviewRequest):
    try:
        features = extract_features(req.code, req.language)
        
        # Check for syntax/parse errors
        if "syntax_error" in features:
            return {
                "bug_probability": 0.0,
                "issues": ["Syntax Error"],
                "suggestions": [f"Fix syntax error: {features['syntax_error']}"],
                "error": features['syntax_error'],
                "language": req.language,
                "features": features
            }
        
        if "parse_error" in features:
            return {
                "bug_probability": 0.0,
                "issues": ["Parse Error"],
                "suggestions": [f"Fix parse error: {features['parse_error']}"],
                "error": features['parse_error'],
                "language": req.language,
                "features": features
            }
        
        if "error" in features:
            return {
                "bug_probability": 0.0,
                "issues": ["Language Error"],
                "suggestions": [features["error"]],
                "error": features["error"],
                "language": req.language,
                "features": features
            }
        
        # deterministic feature ordering
        feature_vector = [features.get("avg_func_len", 0), features.get("loop_count", 0)]
        prob = predict(feature_vector, model=_model)

        issues = []
        suggestions = []
        
        # Language-agnostic checks
        if features.get("avg_func_len", 0) > 50:
            issues.append("Long functions/methods")
            suggestions.append("Consider splitting large functions into smaller units")
        
        if features.get("loop_count", 0) > 5:
            issues.append("Many loops")
            suggestions.append("Consider refactoring nested loops or using built-in functions")
        
        if features.get("function_count", 0) > 20:
            issues.append("High function count")
            suggestions.append("Consider grouping related functions or refactoring into smaller modules")
        
        if features.get("class_count", 0) == 0 and req.language in ["java", "csharp", "c#"]:
            issues.append("No classes defined")
            suggestions.append(f"{req.language.capitalize()} code should be organized in classes")

        return {
            "bug_probability": prob,
            "issues": issues,
            "suggestions": suggestions,
            "language": req.language,
            "features": features,
        }
    
    except Exception as e:
        return {
            "bug_probability": 0.0,
            "issues": ["Processing Error"],
            "suggestions": [str(e)],
            "error": str(e),
            "language": req.language,
        }
