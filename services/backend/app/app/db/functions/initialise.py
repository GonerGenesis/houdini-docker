import logging
import sys

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import TORTOISE_ORM

log = logging.getLogger("uvicorn")

async def init_db(app: FastAPI) -> None:
    fmt = logging.Formatter(
        fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)
    logger_tortoise = logging.getLogger("tortoise")
    logger_tortoise.setLevel(logging.DEBUG)
    logger_tortoise.addHandler(sh)
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )



async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    log.info("Generating database strawberry via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())