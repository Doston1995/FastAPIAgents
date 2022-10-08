from fastapi import APIRouter
from routers import route_agents



api_router = APIRouter()
api_router.include_router(route_agents.router, prefix="/agents",tags=["agents"])