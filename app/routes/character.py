from fastapi import APIRouter
from app.services.character_service import get_character_info

router = APIRouter()


@router.get("/info/{name}")
async def character_info(name: str):
    return await get_character_info(name)
