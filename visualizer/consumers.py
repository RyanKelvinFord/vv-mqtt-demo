import json
import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        asyncio.create_task(self.stream_data())

    async def disconnect(self, close_code):
        pass

    async def stream_data(self):
        while True:
            data = {
                "country_code": "DE",
                "value": round(random.uniform(0, 10), 2)
            }
            await self.send(json.dumps(data))
            await asyncio.sleep(2)