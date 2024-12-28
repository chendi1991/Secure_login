# -*- coding: utf-8 -*-
import uvicorn
from starlette.middleware.cors import CORSMiddleware


from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from fastapi import FastAPI
from app.endpoints import cloud_server
from configs.setting import INIT_HOST, INIT_PORT

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(cloud_server.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
if __name__ == "__main__":
    uvicorn.run("main:app", host=INIT_HOST, port=INIT_PORT, reload=True, debug=True)
