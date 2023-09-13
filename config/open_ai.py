from dotenv import load_dotenv
from classes import OpenAIConfig
import os
import openai
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


config : OpenAIConfig = {
        "model" : os.getenv("OPENAI_MODEL"),
        "max_tokens": int(os.getenv("OPENAI_MAX_TOKENS")),
        "prompt": "Generame una receta de comida con los siguientes ingredientes: "
}

