TrojanChat-Android/app/src/main/java/com/yourorg/trojanchat/Message.kt

package com.yourorg.trojanchat

import kotlinx.serialization.Serializable

@Serializable
data class Message(
    val id: String,
    val sender: String,
    val content: String,
    val timestamp: String
)
