"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import ChatMessage from "./ChatMessage";
import PromptBox from "./PromptBox";
import { sendChatMessage } from "@/lib/api";

type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

const SAMPLE_PROMPTS = [
  "Summarize USC recruiting momentum this week.",
  "Give me a preview of the next USC game.",
  "Who are the biggest roster strengths right now?",
  "What are fans likely discussing most today?",
];

/** Animated three-dot indicator shown while the AI is generating a response. */
function TypingIndicator() {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "flex-start",
        marginBottom: "12px",
      }}
    >
      <div
        style={{
          padding: "12px 18px",
          borderRadius: "14px",
          background: "#1a2233",
          border: "1px solid rgba(255,255,255,0.08)",
          display: "flex",
          gap: "6px",
          alignItems: "center",
        }}
      >
        {[0, 1, 2].map((i) => (
          <span
            key={i}
            style={{
              width: 7,
              height: 7,
              borderRadius: "50%",
              background: "#94a3b8",
              display: "inline-block",
              animation: "tc-bounce 1.2s infinite",
              animationDelay: `${i * 0.2}s`,
            }}
          />
        ))}
        <style>{`
          @keyframes tc-bounce {
            0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
            40% { transform: translateY(-6px); opacity: 1; }
          }
        `}</style>
      </div>
    </div>
  );
}

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content:
        "Welcome to TrojanChat 2.0 AI. Ask me about USC recruiting, game previews, roster analysis, or fan discussion topics. ✌️",
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to the bottom whenever messages or loading state changes
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  const emptyState = useMemo(() => messages.length === 0, [messages.length]);

  async function handleSend(message: string) {
    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: message,
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await sendChatMessage({ message });

      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content:
          response.success && response.response
            ? response.response
            : "I could not generate a response right now. Please try again.",
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      const errorMessage =
        err instanceof Error ? err.message : "Unexpected error";

      setError(errorMessage);

      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content:
            "⚠️ Could not reach the backend. Make sure FastAPI is running on port 8000 and CORS is configured.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div
      style={{
        width: "100%",
        maxWidth: "1000px",
        margin: "0 auto",
        padding: "24px",
      }}
    >
      {/* Header */}
      <div
        style={{
          marginBottom: "20px",
          padding: "20px 24px",
          borderRadius: "18px",
          background:
            "linear-gradient(135deg, rgba(139,0,0,0.4), rgba(20,20,30,0.95))",
          border: "1px solid rgba(255,255,255,0.1)",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <span style={{ fontSize: "28px" }}>🏈</span>
          <div>
            <h1 style={{ margin: 0, fontSize: "26px", fontWeight: 700, lineHeight: 1.2 }}>
              TrojanChat 2.0 AI
            </h1>
            <p style={{ margin: "4px 0 0", color: "#94a3b8", fontSize: "14px" }}>
              Powered by Groq · Cohere · Qdrant · FastAPI · Next.js
            </p>
          </div>
        </div>
      </div>

      {/* Message list */}
      <div
        ref={scrollRef}
        style={{
          minHeight: "420px",
          maxHeight: "60vh",
          overflowY: "auto",
          padding: "18px",
          borderRadius: "18px",
          background: "#0f172a",
          border: "1px solid rgba(255,255,255,0.08)",
          boxShadow: "0 12px 30px rgba(0,0,0,0.25)",
        }}
      >
        {emptyState ? (
          <div style={{ opacity: 0.6, color: "#94a3b8" }}>
            Start the conversation with a USC football question.
          </div>
        ) : (
          messages.map((message) => (
            <ChatMessage
              key={message.id}
              role={message.role}
              content={message.content}
            />
          ))
        )}
        {isLoading && <TypingIndicator />}
      </div>

      {/* Error banner */}
      {error && (
        <div
          style={{
            marginTop: "12px",
            padding: "12px 16px",
            borderRadius: "12px",
            background: "rgba(178,34,34,0.15)",
            border: "1px solid rgba(178,34,34,0.4)",
            color: "#ffd7d7",
            fontSize: "14px",
          }}
        >
          <strong>Error:</strong> {error}
        </div>
      )}

      <PromptBox onSend={handleSend} disabled={isLoading} />

      {/* Sample prompts */}
      <div
        style={{
          marginTop: "18px",
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
          gap: "10px",
        }}
      >
        {SAMPLE_PROMPTS.map((prompt) => (
          <button
            key={prompt}
            onClick={() => {
              if (!isLoading) handleSend(prompt);
            }}
            disabled={isLoading}
            title={prompt}
            style={{
              textAlign: "left",
              padding: "12px 14px",
              borderRadius: "12px",
              border: "1px solid rgba(255,255,255,0.08)",
              background: "#111827",
              color: isLoading ? "#64748b" : "#cbd5e1",
              cursor: isLoading ? "not-allowed" : "pointer",
              fontSize: "13px",
              lineHeight: 1.4,
              transition: "background 0.15s",
            }}
          >
            {prompt}
          </button>
        ))}
      </div>
    </div>
  );
}