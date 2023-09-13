from fastapi import APIRouter
from utils.read_file import get_ingredients as get_ingredients_data
from schemas.ingredients import IngredientsResponse
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ingredients")
def get_ingredients():

    response = {
        "data": get_ingredients_data()
    }

    return response