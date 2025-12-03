"use client";

import { useEffect, useState } from "react";

type Song = {
  id: number;
  title: string;
  artist: string;
};

export default function Home() {
  const [songs, setSongs] = useState<Song[]>([]);
  const [currentSong, setCurrentSong] = useState<Song | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Call backend to get songs
    fetch("http://127.0.0.1:8000/songs")
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Backend error: ${res.status}`);
        }
        return res.json();
      })
      .then((data: Song[]) => {
        setSongs(data);
        if (data.length > 0) {
          setCurrentSong(data[0]);
        }
      })
      .catch((err) => {
        console.error("Error fetching songs:", err);
        setError("Could not load songs from backend.");
      });
  }, []);

  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6">AI Music Player (Prototype)</h1>

      {error && (
        <p className="mb-4 text-red-400 text-sm">
          {error}
        </p>
      )}

      {currentSong ? (
        <div className="mb-8 text-center">
          <p className="text-xs uppercase text-gray-400 tracking-wide">
            Now Playing
          </p>
          <p className="text-2xl font-semibold mt-1">{currentSong.title}</p>
          <p className="text-sm text-gray-300">{currentSong.artist}</p>
        </div>
      ) : !error ? (
        <p className="mb-4 text-gray-300">Loading songs...</p>
      ) : null}

      <div className="w-full max-w-md border border-gray-700 rounded-xl p-4">
        <h2 className="mb-3 font-semibold">Song List</h2>
        {songs.length === 0 && !error && (
          <p className="text-sm text-gray-400">No songs available.</p>
        )}
        <ul className="space-y-2">
          {songs.map((song) => (
            <li
              key={song.id}
              className={`p-2 rounded cursor-pointer ${
                currentSong?.id === song.id
                  ? "bg-gray-700"
                  : "bg-gray-900 hover:bg-gray-800"
              }`}
              onClick={() => setCurrentSong(song)}
            >
              <div className="font-medium">{song.title}</div>
              <div className="text-xs text-gray-400">{song.artist}</div>
            </li>
          ))}
        </ul>
      </div>
    </main>
  );
}
