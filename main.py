from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

# fastapi in lambda needs to especify the subdirectory to load Swagger
app = FastAPI(docs_url='/docs', redoc_url=None)

# this one is  for keeping the lambda warm
@app.get("/warm", include_in_schema=False)
def get_root():
    return {
        "message": "Pong"
    }


@app.get("/ingredients", include_in_schema=False)
def get_root():
    return {
        "message": "Pong"
    }


# allow all methods, probably needs to allow only GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
