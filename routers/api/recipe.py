from typing import List

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from config.open_ai import config as openai_config
from classes import IngredientList
from utils.read_file import get_ingredients as get_ingredients_data
from schemas.ingredients import IngredientsResponse

import openai

router = APIRouter()

@router.post("/recipe")
def get_recipe(ingredientsList: List[IngredientList] = Body(..., embed=True)):
    try:
        
        all_ingredients = []
        for ingredientList in ingredientsList:
            for ingredient in ingredientList['ingredients']:
                all_ingredients.append(ingredient)

        complete_prompt = (
            f"{openai_config['prompt']} {', '.join(all_ingredients)}. "
            "Usa SOLO los ingredientes mencionados. INTENTA USAR TODOS LOS INGREDIENTES. "
            "Recuerda listar los ingredientes y las instrucciones. "
            "Y si no pudiste ocupar ingredientes, mencionalo indicando cuales, pero solo eso, no otro detalle. "
            "Dame SIEMPRE la respuesta con tags html como <h1>, <h2>, <h3>, <p>, <li>, <il>, etc y <br>, y no hagas mención de esto en la respuesta."
        )

        completion = openai.ChatCompletion.create(
            model=openai_config['model'],
            messages=[{"role": "user", "content": complete_prompt}]
        )

        response_data = {"data": completion.choices[0].message.content}

        return JSONResponse(content=response_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
