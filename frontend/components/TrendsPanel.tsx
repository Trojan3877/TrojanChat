"use client";

type Trend = {
  topic: string;
  category: string;
  heat: "��🔥🔥" | "🔥🔥" | "🔥";
};

const TRENDING_TOPICS: Trend[] = [
  { topic: "QB competition heading into spring camp", category: "Roster", heat: "🔥🔥🔥" },
  { topic: "Defensive line depth chart update", category: "Roster", heat: "🔥🔥🔥" },
  { topic: "2025 recruiting class rankings", category: "Recruiting", heat: "🔥🔥" },
  { topic: "Big Ten schedule preview", category: "Schedule", heat: "🔥🔥" },
  { topic: "Transfer portal targets this cycle", category: "Recruiting", heat: "🔥" },
];

const CATEGORY_COLORS: Record<string, string> = {
  Roster: "#a78bfa",
  Recruiting: "#34d399",
  Schedule: "#60a5fa",
};

export default function TrendsPanel() {
  return (
    <div style={{ padding: "20px" }}>
      <h2 style={{ marginBottom: "8px" }}>📈 Trending Fan Topics</h2>
      <p style={{ marginBottom: "20px", opacity: 0.7, fontSize: "14px" }}>
        Topics gaining traction across USC fan communities right now.
      </p>

      <div style={{ display: "grid", gap: "10px" }}>
        {TRENDING_TOPICS.map((t) => (
          <div
            key={t.topic}
            style={{
              padding: "14px 16px",
              borderRadius: "12px",
              background: "#111827",
              border: "1px solid rgba(255,255,255,0.07)",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              gap: "12px",
            }}
          >
            <div>
              <div style={{ fontWeight: 500, marginBottom: "4px" }}>{t.topic}</div>
              <span
                style={{
                  fontSize: "11px",
                  fontWeight: 700,
                  padding: "2px 8px",
                  borderRadius: "10px",
                  background: `${CATEGORY_COLORS[t.category] ?? "#6b7280"}22`,
                  color: CATEGORY_COLORS[t.category] ?? "#6b7280",
                }}
              >
                {t.category}
              </span>
            </div>
            <span style={{ fontSize: "18px", flexShrink: 0 }}>{t.heat}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
