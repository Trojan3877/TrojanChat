import pytest
from httpx import AsyncClient, ASGITransport
from backend.api import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "TrojanChat API is running" in response.text
