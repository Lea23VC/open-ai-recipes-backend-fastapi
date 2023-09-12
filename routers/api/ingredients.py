from fastapi import APIRouter, Depends, HTTPException
from api import router


@router.get("/ingredients")
def get_ingredients():
    return {
        "message": "Pong"
    }