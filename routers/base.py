from fastapi import APIRouter
from routers import route_agents, route_customers



api_router = APIRouter()
api_router.include_router(route_agents.router, prefix="/agents",tags=["agents"])
api_router.include_router(route_customers.router, prefix="/customers",tags=["customers"])