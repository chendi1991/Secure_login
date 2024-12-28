# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from jose import jwt
from starlette import status

from models.models import User

form_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

SECRET_KEY = "dc393487a84ddf9da61fe0180ef295cf0642ecbc5d678a1589ef2e26b35fce9c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 43200


def create_token(user: User, expires_delta: Optional[timedelta]):
    expire = datetime.utcnow() + expires_delta or timedelta(minutes=15)
    return jwt.encode(
        claims={"sub": user.username, "exp": expire},
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )
