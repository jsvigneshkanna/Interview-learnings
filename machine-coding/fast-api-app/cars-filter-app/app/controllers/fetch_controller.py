from fastapi import APIRouter, Query

router = APIRouter()

@router.get('/cars/')
async def get_cars():
    return "vignesh here"