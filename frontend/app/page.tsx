import ChatWindow from "@/components/ChatWindow";

export default function HomePage() {
  return (
    <main
      style={{
        minHeight: "100vh",
        padding: "32px 16px",
        background:
          "radial-gradient(circle at top, rgba(128,0,0,0.22), transparent 35%), #0b0f19",
      }}
    >
      <ChatWindow />
    </main>
  );
}