import httpx
from typing import Any, Dict

BASE_URL = "https://api.tibiadata.com/v4/"

async def fetch_tibiadata(endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:

    url = f"{BASE_URL}{endpoint}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status() 
        return response.json()
