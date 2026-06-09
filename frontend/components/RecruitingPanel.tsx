"use client";

type Recruit = {
  name: string;
  position: string;
  stars: number;
  status: "Committed" | "Visiting" | "Offer Extended";
};

const SAMPLE_RECRUITS: Recruit[] = [
  { name: "Marcus Thompson", position: "QB", stars: 5, status: "Committed" },
  { name: "DeAndre Williams", position: "WR", stars: 4, status: "Committed" },
  { name: "Jordan Hayes", position: "OL", stars: 4, status: "Visiting" },
  { name: "Tyler Brooks", position: "CB", stars: 4, status: "Offer Extended" },
];

const STATUS_COLORS: Record<Recruit["status"], string> = {
  Committed: "#22c55e",
  Visiting: "#f59e0b",
  "Offer Extended": "#3b82f6",
};

export default function RecruitingPanel() {
  return (
    <div style={{ padding: "20px" }}>
      <h2 style={{ marginBottom: "8px" }}>⭐ USC Recruiting Tracker</h2>
      <p style={{ marginBottom: "20px", opacity: 0.7, fontSize: "14px" }}>
        AI-assisted recruiting summaries. Data reflects sample pipeline state.
      </p>

      <div style={{ display: "grid", gap: "12px" }}>
        {SAMPLE_RECRUITS.map((r) => (
          <div
            key={r.name}
            style={{
              padding: "14px 16px",
              borderRadius: "12px",
              background: "#111827",
              border: "1px solid rgba(255,255,255,0.07)",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <div style={{ fontWeight: 600, marginBottom: "4px" }}>{r.name}</div>
              <div style={{ fontSize: "13px", opacity: 0.6 }}>
                {r.position} · {"★".repeat(r.stars)}
              </div>
            </div>
            <span
              style={{
                fontSize: "12px",
                fontWeight: 700,
                padding: "4px 10px",
                borderRadius: "20px",
                background: `${STATUS_COLORS[r.status]}22`,
                color: STATUS_COLORS[r.status],
                border: `1px solid ${STATUS_COLORS[r.status]}55`,
              }}
            >
              {r.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
