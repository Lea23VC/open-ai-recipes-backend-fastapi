
from fastapi import APIRouter
from routers.api.ingredients import router as ingredients_router

router = APIRouter(prefix="/api")

router.include_router(ingredients_router)