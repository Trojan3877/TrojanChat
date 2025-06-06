TrojanChat-Android/app/src/main/java/com/yourorg/trojanchat/WebSocketClient.kt

package com.yourorg.trojanchat

import okhttp3.*
import okio.ByteString
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.util.*

class WebSocketClient(private val listener: (Message) -> Unit) {
    private val client = OkHttpClient()
    private lateinit var webSocket: WebSocket

    fun connect() {
        val request = Request.Builder()
            .url("ws://10.0.2.2:8080/chat")
            .build()
        webSocket = client.newWebSocket(request, object : WebSocketListener() {
            override fun onMessage(webSocket: WebSocket, text: String) {
                val msg = Json.decodeFromString<Message>(text)
                listener(msg)
            }
            override fun onMessage(webSocket: WebSocket, bytes: ByteString) { /* no-op */ }
            override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {
                t.printStackTrace()
            }
        })
    }

    fun send(content: String) {
        val msg = Message(
            id = UUID.randomUUID().toString(),
            sender = "AndroidUser",
            content = content,
            timestamp = Date().toString()
        )
        val text = Json.encodeToString(msg)
        webSocket.send(text)
    }

    fun close() {
        webSocket.close(1000, "App closed")
        client.dispatcher.executorService.shutdown()
    }
}
