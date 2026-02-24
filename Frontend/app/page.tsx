"use client";
import { useState } from "react";
import { api } from "../lib/api";
import SearchBar from "../components/SearchBar";
import VideoCard from "../components/VideoCard";

export default function Home() {
  const [results, setResults] = useState([]);

  const search = async (query: string) => {
    const res = await api.get("/search", { params: { q: query } });
    setResults(res.data);
  };

  return (
    <div className="bg-black min-h-screen">
      <SearchBar onSearch={search} />
      {results.map((video: any, i) => (
        <VideoCard key={i} video={video} />
      ))}
    </div>
  );
}
