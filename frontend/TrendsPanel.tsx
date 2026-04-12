"use client";

export default function TrendsPanel() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>📈 Trending Fan Topics</h2>

      <div
        style={{
          marginTop: "20px",
          display: "grid",
          gap: "12px",
        }}
      >
        {[
          "QB competition heating up",
          "Defensive line depth",
          "Recruiting class rankings",
        ].map((trend) => (
          <div
            key={trend}
            style={{
              padding: "14px",
              borderRadius: "10px",
              background: "#111827",
            }}
          >
            {trend}
          </div>
        ))}
      </div>
    </div>
  );
}