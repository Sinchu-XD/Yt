"use client";
import { useEffect, useState } from "react";
import { api } from "../lib/api";
import Link from "next/link";

export default function Suggestions({ title, url }: any) {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    api.get("/suggest", { params: { title, url } })
      .then(res => setVideos(res.data));
  }, []);

  return (
    <div className="w-80">
      {videos.map((v: any, i) => (
        <Link key={i} href={`/watch?url=${encodeURIComponent(v.url)}`}>
          <div className="flex gap-2 mb-4 cursor-pointer">
            <img src={v.thumbnail} className="w-32 h-20 object-cover rounded"/>
            <div>
              <p className="text-white text-sm">{v.title}</p>
              <p className="text-gray-400 text-xs">{v.channel}</p>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
