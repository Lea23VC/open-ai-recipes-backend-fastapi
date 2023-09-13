from fastapi import APIRouter
from utils.read_file import get_ingredients as get_ingredients_data
from schemas.ingredients import IngredientsResponse
from fastapi.responses import JSONResponse
import openai
from config.open_ai import config as openai_config

router = APIRouter()

@router.post("/recipe")
def get_recipe():
    complete_prompt = (openai_config["prompt"] + " naranjas")
    completion = openai.ChatCompletion.create(model=openai_config["model"], 
                                              messages=[{"role": "user", "content": complete_prompt}])
    return JSONResponse({"data": completion})