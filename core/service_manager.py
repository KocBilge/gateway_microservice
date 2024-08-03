from httpx import AsyncClient

class ServiceManager:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = AsyncClient()

    async def get(self, path: str):
        url = f"{self.base_url}{path}"
        response = await self.client.get(url)
        response.raise_for_status()
        return response.json()

    async def post(self, path: str, data: dict):
        url = f"{self.base_url}{path}"
        response = await self.client.post(url, json=data)
        response.raise_for_status()
        return response.json()
