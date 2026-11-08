from fastapi import FastAPI

from app.api.routes import health, meta

def create_app() -> FastAPI:
    app = FastAPI(title="My FastAPI Application", version="1.0.0")  #-- creates an instance of the FastAPI application with a title and version
    app.include_router(health.router)
    app.include_router(meta.router)   #-- plugs the router into the app. Forget this and you get a 404.
    return app

app = create_app()