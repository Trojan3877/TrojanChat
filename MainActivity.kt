TrojanChat-Android/app/src/main/java/com/yourorg/trojanchat/MainActivity.kt

package com.yourorg.trojanchat

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import androidx.core.view.setPadding

class MainActivity : AppCompatActivity() {
    private lateinit var webSocketClient: WebSocketClient
    private lateinit var messagesLayout: LinearLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        messagesLayout = findViewById(R.id.messagesLayout)
        val messageInput: EditText = findViewById(R.id.messageInput)
        val sendButton: Button = findViewById(R.id.sendButton)

        webSocketClient = WebSocketClient { msg ->
            runOnUiThread {
                val tv = TextView(this)
                tv.text = "${msg.sender}: ${msg.content}"
                tv.setPadding(8)
                messagesLayout.addView(tv)
            }
        }
        webSocketClient.connect()

        sendButton.setOnClickListener {
            val content = messageInput.text.toString()
            if (content.isNotEmpty()) {
                webSocketClient.send(content)
                messageInput.text.clear()
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        webSocketClient.close()
    }
}
