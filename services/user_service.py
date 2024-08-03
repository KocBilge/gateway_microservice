from core.service_manager import ServiceManager
from config import settings

class UserService:
    def __init__(self):
        self.manager = ServiceManager(settings.USER_SERVICE_URL)

    async def get_user(self, user_id: int):
        return await self.manager.get(f"/users/{user_id}")

    async def create_user(self, user_data: dict):
        return await self.manager.post("/users", user_data)
