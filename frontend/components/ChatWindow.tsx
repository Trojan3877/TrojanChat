"use client";

import { useMemo, useState } from "react";
import ChatMessage from "./ChatMessage";
import PromptBox from "./PromptBox";
import { sendChatMessage } from "@/lib/api";

type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content:
        "Welcome to TrojanChat 2.0 AI. Ask me about USC recruiting, game previews, roster analysis, or fan discussion topics.",
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

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
            : "I could not generate a response right now.",
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
            "There was a connection issue talking to the backend. Check that FastAPI is running and CORS is configured correctly.",
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
      <div
        style={{
          marginBottom: "20px",
          padding: "20px",
          borderRadius: "18px",
          background:
            "linear-gradient(135deg, rgba(139,0,0,0.35), rgba(20,20,30,0.9))",
          border: "1px solid rgba(255,255,255,0.08)",
        }}
      >
        <h1
          style={{
            margin: 0,
            fontSize: "32px",
            lineHeight: 1.1,
          }}
        >
          TrojanChat 2.0 AI
        </h1>
        <p
          style={{
            marginTop: "10px",
            marginBottom: 0,
            color: "#d7dbe5",
            fontSize: "16px",
          }}
        >
          AI-powered USC fan intelligence platform using Next.js, FastAPI,
          Groq, Cohere, and Qdrant.
        </p>
      </div>

      <div
        style={{
          minHeight: "500px",
          maxHeight: "65vh",
          overflowY: "auto",
          padding: "18px",
          borderRadius: "18px",
          background: "#0f172a",
          border: "1px solid rgba(255,255,255,0.08)",
          boxShadow: "0 12px 30px rgba(0,0,0,0.25)",
        }}
      >
        {emptyState ? (
          <div style={{ opacity: 0.8 }}>
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
      </div>

      {error && (
        <div
          style={{
            marginTop: "12px",
            padding: "12px 14px",
            borderRadius: "12px",
            background: "rgba(178,34,34,0.15)",
            border: "1px solid rgba(178,34,34,0.4)",
            color: "#ffd7d7",
          }}
        >
          {error}
        </div>
      )}

      <PromptBox onSend={handleSend} disabled={isLoading} />

      <div
        style={{
          marginTop: "18px",
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
          gap: "12px",
        }}
      >
        {[
          "Summarize USC recruiting momentum this week.",
          "Give me a preview of the next USC game.",
          "Who are the biggest roster strengths right now?",
          "What are fans likely discussing most today?",
        ].map((prompt) => (
          <button
            key={prompt}
            onClick={() => {
              if (!isLoading) {
                handleSend(prompt);
              }
            }}
            style={{
              textAlign: "left",
              padding: "14px",
              borderRadius: "14px",
              border: "1px solid rgba(255,255,255,0.08)",
              background: "#111827",
              color: "#ffffff",
              cursor: isLoading ? "not-allowed" : "pointer",
            }}
            disabled={isLoading}
          >
            {prompt}
          </button>
        ))}
      </div>
    </div>
  );
}