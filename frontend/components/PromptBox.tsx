"use client";

import { useState } from "react";

type PromptBoxProps = {
  onSend: (message: string) => Promise<void>;
  disabled?: boolean;
};

export default function PromptBox({
  onSend,
  disabled = false,
}: PromptBoxProps) {
  const [message, setMessage] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    const trimmed = message.trim();
    if (!trimmed || disabled) return;

    setMessage("");
    await onSend(trimmed);
  }

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: "flex",
        gap: "10px",
        marginTop: "16px",
      }}
    >
      <input
        type="text"
        placeholder="Ask about USC recruiting, game recaps, roster analysis..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={disabled}
        style={{
          flex: 1,
          padding: "14px",
          borderRadius: "12px",
          border: "1px solid rgba(255,255,255,0.12)",
          background: "#111827",
          color: "#ffffff",
          outline: "none",
        }}
      />
      <button
        type="submit"
        disabled={disabled}
        style={{
          padding: "14px 18px",
          borderRadius: "12px",
          border: "none",
          background: disabled ? "#555" : "#b22222",
          color: "#fff",
          cursor: disabled ? "not-allowed" : "pointer",
          fontWeight: 700,
        }}
      >
        {disabled ? "Sending..." : "Send"}
      </button>
    </form>
  );
}