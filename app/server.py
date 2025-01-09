import asyncio
import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from loguru import logger
from app.router import nyi
from contextlib import asynccontextmanager

from utils.WatchFolder import WatchFolder
from utils import AppSettings

settings = AppSettings.AppSettings()


async def print_task(s):
    while True:
        logger.info("Hello")
        await asyncio.sleep(s)


@asynccontextmanager
async def lifespan(app: FastAPI):
    ###  before the application starts ###
    os.makedirs("./data/log", exist_ok=True)
    os.makedirs("./data/upload", exist_ok=True)
    logger.add(
        settings.LOG_FILE,
        colorize=False,
        enqueue=True,
        level=os.getenv("LOGLEVEL", default="DEBUG"),
        rotation="1 MB",
    )
    logger.success(f"Starting server with loglevel: {settings.LOG_LEVEL}")
    watchfolder = WatchFolder("./data/upload")
    asyncio.create_task(watchfolder.start())

    ### after the application has finished ###
    yield
    # watchfolder.stop()
    logger.success("Server has shut down.")


app = FastAPI(
    title=settings.fastapi_title,
    version=settings.fastapi_version,
    description=settings.fastapi_description,
    lifespan=lifespan,
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# @app.get("/nyi", description="Platzhalter")
# def nyi():
#     return {"output": "nyi"}


app.include_router(nyi.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
