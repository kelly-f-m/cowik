from fastapi import APIRouter
from app.services.rashid_service import rashid_location

router = APIRouter()


@router.get("/rashid")
async def get_rashid_location():
    """
    Endpoint that returns Rashid's location based on the current weekday.
    """
    return rashid_location()
