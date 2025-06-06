import SwiftUI

@main
struct TrojanChatApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

import SwiftUI

struct ContentView: View {
    @ObservedObject var webSocket = WebSocketService()
    @State private var messageText: String = ""

    var body: some View {
        NavigationView {
            VStack {
                ScrollView {
                    ForEach(webSocket.messages) { msg in
                        HStack {
                            Text(msg.sender)
                                .font(.caption)
                                .foregroundColor(.gray)
                            Text(msg.content)
                                .padding(8)
                                .background(Color.blue.opacity(0.1))
                                .cornerRadius(8)
                            Spacer()
                        }
                        .padding(.horizontal)
                    }
                }
                HStack {
                    TextField("Enter message...", text: $messageText)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    Button("Send") {
                        guard !messageText.isEmpty else { return }
                        webSocket.send(messageText)
                        messageText = ""
                    }
                }
                .padding()
            }
            .navigationTitle("Trojan Chat")
        }
        .onAppear {
            webSocket.connect()
        }
    }
}

import Foundation

struct Message: Identifiable, Codable {
    let id: UUID
    let sender: String
    let content: String
    let timestamp: Date
}

import Foundation
import Combine

class WebSocketService: ObservableObject {
    @Published var messages: [Message] = []
    private var webSocketTask: URLSessionWebSocketTask?

    func connect() {
        guard let url = URL(string: "ws://localhost:8080/chat") else { return }
        webSocketTask = URLSession.shared.webSocketTask(with: url)
        webSocketTask?.resume()
        receive()
    }

    func send(_ content: String) {
        let msg = Message(id: UUID(),
                          sender: "iOSUser",
                          content: content,
                          timestamp: Date())
        guard let data = try? JSONEncoder().encode(msg),
              let text = String(data: data, encoding: .utf8) else { return }
        webSocketTask?.send(.string(text)) { error in
            if let err = error { print("WebSocket send error: \(err)") }
        }
    }

    private func receive() {
        webSocketTask?.receive { [weak self] result in
            switch result {
            case .failure(let error):
                print("WebSocket receive error: \(error)")
            case .success(.string(let text)):
                if let data = text.data(using: .utf8),
                   let msg = try? JSONDecoder().decode(Message.self, from: data) {
                    DispatchQueue.main.async {
                        self?.messages.append(msg)
                    }
                }
            default:
                break
            }
            self?.receive()
        }
    }
}

