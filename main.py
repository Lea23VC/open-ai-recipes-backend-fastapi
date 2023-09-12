from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from routers.api import router as api_router

# fastapi in lambda needs to especify the subdirectory to load Swagger
app = FastAPI(docs_url='/docs', redoc_url=None)
#


app.include_router(api_router)

# allow all methods, probably needs to allow only GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
