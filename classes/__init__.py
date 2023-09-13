from typing import TypedDict

class IngredientsDict(TypedDict):
    fruits : list[str]
    vegetables : list[str]
    nuts : list[str]
    bread_and_cereals : list[str]
    dairies : list[str]
    meats_and_proteins : list[str]
    fats : list[str]
    seasonings_and_flavorings : list[str]


class OpenAIConfig(TypedDict):
    api_key : str
    engine : str
    model: str
    max_tokens : int