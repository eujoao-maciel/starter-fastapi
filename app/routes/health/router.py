from fastapi import APIRouter
from app.routes.health.schemas import HealthResponse

router = APIRouter(tags=["Health"])

@router.get("/health", summary="Health Check", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="server on")

