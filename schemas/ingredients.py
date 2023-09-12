from pydantic import BaseModel


class Ingredients(BaseModel):
    fruits : list[str]
    vegetables : list[str]
    nuts : list[str]
    bread_and_cereals : list[str]
    dairies : list[str]
    meats_and_proteins : list[str]
    fats : list[str]
    seasonings_and_flavorings : list[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientsResponse(BaseModel):
    data : Ingredients

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
