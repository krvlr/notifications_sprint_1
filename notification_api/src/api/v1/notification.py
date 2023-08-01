import logging

from fastapi import APIRouter, Depends

logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "OK"}
