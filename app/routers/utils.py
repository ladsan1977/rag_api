from fastapi import APIRouter

router = APIRouter()

@router.get("/utils/ping")
def ping_utils():
    return {"message": "Utils router OK"}
