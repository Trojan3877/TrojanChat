import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "TrojanChat 2.0 AI",
  description: "AI-powered USC fan platform with FastAPI + Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}