from fastapi import APIRouter, Depends, HTTPException
from services.user_service import UserService

router = APIRouter()

async def get_user_service():
    return UserService()

@router.get("/{user_id}")
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        return await service.get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
