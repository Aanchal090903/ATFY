"use client";

import { useEffect, useState } from "react";
import { API_BASE } from "@/lib/api";
import Link from "next/link";

export default function Home() {
  const [title, setTitle] = useState("");
  const [scrapbooks, setScrapbooks] = useState<any[]>([]);

  useEffect(() => {
    fetch(`${API_BASE}/scrapbooks`)
      .then(res => res.json())
      .then(data => setScrapbooks(data.items || []));
  }, []);

  async function createScrapbook() {
    if (!title.trim()) return;

    const res = await fetch(`${API_BASE}/scrapbooks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title })
    });

    const data = await res.json();
    setScrapbooks(prev => [...prev, data]);
    setTitle("");
  }

  return (
    <main className="p-8 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">OnYourDesk</h1>

      <input
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="Create a new scrapbook"
        className="border p-2 w-full mb-2"
      />

      <button
        onClick={createScrapbook}
        className="bg-black text-white px-4 py-2 mb-8"
      >
        Create Scrapbook
      </button>

      <ul className="space-y-3">
        {scrapbooks.map(sb => (
          <li key={sb.id}>
            <Link
              href={`/scrapbook/${sb.id}`}
              className="underline text-lg"
            >
              {sb.title}
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
