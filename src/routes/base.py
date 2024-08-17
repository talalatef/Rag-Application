from fastapi import FastAPI, APIRouter
from helpers.config import get_settings

base_route = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_route.get('/')
async def welcome():
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    version_app = app_settings.VERSION_APP
    return {
        "app_name" : app_name,
        "version_app" : version_app
    }