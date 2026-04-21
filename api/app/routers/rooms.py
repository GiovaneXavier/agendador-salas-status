from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.room import RoomStatusResponse
from app.services import status_service

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/status", response_model=list[RoomStatusResponse])
async def list_rooms_status(db: AsyncSession = Depends(get_db)):
    return await status_service.get_all_rooms_status(db)


@router.get("/status/{room_id}", response_model=RoomStatusResponse)
async def get_room_status(room_id: str, db: AsyncSession = Depends(get_db)):
    room = await status_service.get_room_status(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    return room
