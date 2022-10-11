from fastapi import FastAPI
from core.config import settings
from routers.base import api_router
from db.session import engine
from db.models import Base
from starlette.middleware.cors import CORSMiddleware
from db.utils import check_db_connected, check_db_disconnected

def include_router(app):
    app.include_router(api_router, prefix="/api/v1")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app 


app = start_application()

@app.on_event("startup")
async def app_startup():
    await check_db_connected()
    
    
@app.on_event("shutdown")     
async def app_shutdown():
    await check_db_disconnected()