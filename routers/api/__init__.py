
from fastapi import APIRouter
from routers.api.ingredients import router as ingredients_router
from routers.api.recipe import router as recipe_router

router = APIRouter(prefix="/api")

router.include_router(ingredients_router)
router.include_router(recipe_router)