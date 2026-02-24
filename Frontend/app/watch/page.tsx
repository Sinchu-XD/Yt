"use client";
import { useSearchParams } from "next/navigation";

export default function WatchPage() {
  const params = useSearchParams();
  const url = params.get("url");

  return (
    <div className="bg-black min-h-screen p-6">
      <video
        controls
        autoPlay
        className="w-full max-w-4xl"
        src={`http://localhost:8000/api/watch?url=${encodeURIComponent(
          url || ""
        )}`}
      />
    </div>
  );
}
