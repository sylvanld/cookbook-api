from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import cookbook.api.healthcheck
import cookbook.api.v1.groups
import cookbook.api.v1.ingredients
import cookbook.api.v1.lists
import cookbook.api.v1.recipes
from cookbook.api.metadata import API_DESCRIPTION, API_TAGS, API_TITLE, API_VERSION
from cookbook.core.config import Config


def create_api(config: Config):
    app = FastAPI(
        title=API_TITLE, version=API_VERSION, description=API_DESCRIPTION, openapi_tags=API_TAGS, docs_url="/"
    )
    app.add_middleware(CORSMiddleware, allow_origins="*", allow_methods="*", allow_headers="*", allow_credentials=True)

    app.include_router(cookbook.api.healthcheck.router)
    app.include_router(cookbook.api.v1.groups.router, tags=["groups"], prefix="/v1")
    app.include_router(cookbook.api.v1.ingredients.router, tags=["ingredients"], prefix="/v1")
    app.include_router(cookbook.api.v1.lists.router, tags=["lists"], prefix="/v1")
    app.include_router(cookbook.api.v1.recipes.router, tags=["recipes"], prefix="/v1")

    return app
