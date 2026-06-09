type ChatMessageProps = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatMessage({
  role,
  content,
}: ChatMessageProps) {
  const isUser = role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: "12px",
      }}
    >
      <div
        style={{
          maxWidth: "75%",
          padding: "12px 14px",
          borderRadius: "14px",
          background: isUser ? "#8b0000" : "#1a2233",
          color: "#ffffff",
          lineHeight: 1.5,
          whiteSpace: "pre-wrap",
          border: "1px solid rgba(255,255,255,0.08)",
        }}
      >
        <div
          style={{
            fontSize: "12px",
            opacity: 0.75,
            marginBottom: "6px",
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.04em",
          }}
        >
          {isUser ? "You" : "TrojanChat AI"}
        </div>
        <div>{content}</div>
      </div>
    </div>
  );
}