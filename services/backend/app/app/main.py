from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

import logging

from app.strawberry.__init__ import graphql_app
from .db.functions.initialise import init_db


log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["https://localhost", "http://localhost", "http://0.0.0.0:5174", "http://frontend", "http://0.0.0.0:5173", "http://localhost:5173",
                       "http://localhost:8080", "http://127.0.0.1:5174", "http://localhost:5174", "http://172.22.0.3:5174"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(graphql_app, prefix='/graphql')

    @application.get("/")
    async def root():
        return {"message": "Hello World"}

    @application.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    await init_db(app)

    # frame = await Frame.all()
    # log.info(Ship.fetch_related())


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
