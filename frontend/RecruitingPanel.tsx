"use client";

export default function RecruitingPanel() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>⭐ USC Recruiting Insights</h2>

      <p style={{ marginTop: "10px", opacity: 0.8 }}>
        AI-powered recruiting summaries and analysis.
      </p>

      <div
        style={{
          marginTop: "20px",
          padding: "16px",
          borderRadius: "12px",
          background: "#111827",
        }}
      >
        <p>
          Example:
          <br />
          USC is trending positively with multiple 4-star recruits this week...
        </p>
      </div>
    </div>
  );
}