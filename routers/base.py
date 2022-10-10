from fastapi import APIRouter
from routers import route_agents, route_customers, route_orders, route_users



api_router = APIRouter()
api_router.include_router(route_agents.router, prefix="/agents",tags=["agents"])
api_router.include_router(route_customers.router, prefix="/customers",tags=["customers"])
api_router.include_router(route_orders.router, prefix="/orders",tags=["orders"])
api_router.include_router(route_users.router, prefix="/users",tags=["users"])