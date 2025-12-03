from fastapi import FastAPI
from typing import List, Dict

app = FastAPI(title="AI Music Player Backend")

SONGS = [
    {"id": 1, "title": "Snowy Night Vibes", "artist": "Demo Artist"},
    {"id": 2, "title": "Chill Study Beat", "artist": "Demo Artist"},
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/songs")
def get_songs() -> List[Dict]:
    return SONGS