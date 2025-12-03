from .db import Base, engine, SessionLocal
from .models import Song

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:

        count = db.query(Song).count()
        if count == 0:
            demo_songs = [
                {
                    "title": "Snowy Night Vibes",
                    "artist": "Demo Artist",
                    "lyrics": "Snow is falling, lights are glowing...",
                },
                {
                    "title": "Chill Study Beat",
                    "artist": "Demo Artist",
                    "lyrics": "Focus on the rhythm, let your mind flow...",
                },
                {
                    "title": "Lo-Fi Study Flow",
                    "artist": "Demo Artist",
                    "lyrics": "Beats that help you concentrate and relax...",
                }
            ]

            for s in demo_songs:
                db.add(Song(**s))

            db.commit()
            print("Seeded demo songs into the database.")

        else:
            print
            (f"Database already has {count} song(s), skipping seed.")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()