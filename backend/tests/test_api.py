import pytest
from httpx import AsyncClient
from backend.api import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "TrojanChat API is running" in response.text
