# app/core/redis_manager.py

import asyncio
import json
import os
import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)


class RedisPubSubManager:
    def __init__(self):
        self.pubsub = redis_client.pubsub()
        self.channel = "trojan_chat"

    async def connect(self):
        await self.pubsub.subscribe(self.channel)

    async def publish(self, message: dict):
        await redis_client.publish(self.channel, json.dumps(message))

    async def listen(self):
        async for msg in self.pubsub.listen():
            if msg["type"] == "message":
                yield json.loads(msg["data"])