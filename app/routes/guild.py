from fastapi import APIRouter
from app.services.guild_service import get_guild_info

router = APIRouter()


@router.get("/info/{name}")
async def guild_info(name: str):
    return await get_guild_info(name)
