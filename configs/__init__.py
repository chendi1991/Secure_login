from .logging_set import logger
import redis
from fastapi import FastAPI
from configs import setting
from fastapi.staticfiles import StaticFiles
from app.endpoints import cloud_server
from fastapi.middleware.cors import CORSMiddleware


def init_app():
    logger.info("init  db_connect----->")
    redis.Redis()
    logger.info("init  fastapi.....")
    app = FastAPI()
    logger.info("init  staticFiles.....")
    app.mount("/images", StaticFiles(directory='/xxx/xxx/images'), name='images')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"]
    )
    logger.info("init  router.....")
    app.include_router(cloud_server.router)
    return app
