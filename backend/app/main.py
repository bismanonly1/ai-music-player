from fastapi import FastAPI
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Music Player Backend")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SONGS = [
    {"id": 1, "title": "Snowy Night Vibes", "artist": "Demo Artist"},
    {"id": 2, "title": "Chill Study Beat", "artist": "Demo Artist"},
    {"id": 3, "title": "Lo-Fi Study Flow", "artist": "Demo Artist"},
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/songs")
def get_songs() -> List[Dict]:
    return SONGS