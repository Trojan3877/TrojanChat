"use client";

type Tab = "chat" | "recruiting" | "trends";

export default function Sidebar({
  activeTab,
  setActiveTab,
}: {
  activeTab: Tab;
  setActiveTab: (tab: Tab) => void;
}) {
  const tabs: { key: Tab; label: string }[] = [
    { key: "chat", label: "💬 Chat" },
    { key: "recruiting", label: "⭐ Recruiting" },
    { key: "trends", label: "📈 Trends" },
  ];

  return (
    <div
      style={{
        width: "240px",
        background: "#0f172a",
        padding: "20px",
        borderRight: "1px solid rgba(255,255,255,0.08)",
      }}
    >
      <h2 style={{ marginBottom: "20px", color: "#b22222" }}>
        TrojanChat AI
      </h2>

      {tabs.map((tab) => (
        <div
          key={tab.key}
          onClick={() => setActiveTab(tab.key)}
          style={{
            padding: "12px",
            marginBottom: "10px",
            borderRadius: "10px",
            cursor: "pointer",
            background:
              activeTab === tab.key ? "#b22222" : "transparent",
          }}
        >
          {tab.label}
        </div>
      ))}
    </div>
  );
}