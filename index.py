from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load CSV once at startup
df = pd.read_csv("api/data.csv")  # Adjusted path

@app.get("/api")
def read_students(request: Request):
    classes = request.query_params.getlist("class")
    if classes:
        filtered = df[df["class"].isin(classes)]
    else:
        filtered = df
    return {
        "students": filtered.to_dict(orient="records")
    }
