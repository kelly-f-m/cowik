from fastapi import APIRouter
from .character import router as character
from .guild import router as guild
from .rashid import router as rashid
from .home import router as home

api_router = APIRouter()

api_router.include_router(character, prefix="/character", tags=["Character"])
api_router.include_router(guild, prefix="/guild", tags=["Guild"])
api_router.include_router(rashid, prefix="", tags=["Rashid"])
api_router.include_router(home, prefix="", tags=["Home"])
