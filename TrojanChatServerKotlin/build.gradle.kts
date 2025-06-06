TrojanChatServerKotlin/build.gradle.kts

plugins {
    kotlin("jvm") version "1.7.10"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-server-core:2.3.0")
    implementation("io.ktor:ktor-server-netty:2.3.0")
    implementation("io.ktor:ktor-server-websockets:2.3.0")
    implementation("io.ktor:ktor-serialization-kotlinx-json:2.3.0")
    implementation("ch.qos.logback:logback-classic:1.2.11")
}

application {
    mainClass.set("com.yourorg.trojanchat.ApplicationKt")
}
