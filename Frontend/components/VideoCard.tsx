import Link from "next/link";

export default function VideoCard({ video }: any) {
  return (
    <Link href={`/watch?url=${encodeURIComponent(video.url)}`}>
      <div className="flex gap-4 p-4 hover:bg-gray-800 cursor-pointer">
        <img
          src={video.thumbnail}
          className="w-60 h-36 object-cover rounded"
        />
        <div>
          <h2 className="text-white text-lg">{video.title}</h2>
          <p className="text-gray-400">{video.channel}</p>
          <p className="text-gray-500 text-sm">{video.views} views</p>
        </div>
      </div>
    </Link>
  );
}
