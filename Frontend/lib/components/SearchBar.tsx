"use client";
import { useState } from "react";

export default function SearchBar({ onSearch }: any) {
  const [query, setQuery] = useState("");

  return (
    <div className="flex justify-center p-4">
      <input
        className="w-1/2 p-3 rounded-l bg-gray-800 text-white"
        placeholder="Search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        className="bg-red-600 px-6 rounded-r"
        onClick={() => onSearch(query)}
      >
        Search
      </button>
    </div>
  );
}
