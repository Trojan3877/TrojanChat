"use client";

import { useState } from "react";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import RecruitingPanel from "@/components/RecruitingPanel";
import TrendsPanel from "@/components/TrendsPanel";

type Tab = "chat" | "recruiting" | "trends";

export default function HomePage() {
  const [activeTab, setActiveTab] = useState<Tab>("chat");

  return (
    <main
      style={{
        display: "flex",
        height: "100vh",
        background: "#0b0f19",
      }}
    >
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      <div style={{ flex: 1, overflow: "auto" }}>
        {activeTab === "chat" && <ChatWindow />}
        {activeTab === "recruiting" && <RecruitingPanel />}
        {activeTab === "trends" && <TrendsPanel />}
      </div>
    </main>
  );
}