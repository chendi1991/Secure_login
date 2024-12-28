# -*- coding: utf-8 -*-
import time
from datetime import datetime
from datetime import timedelta
from typing import Optional

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from mongoengine import *
from starlette import status


from models.models import User

connect(**MONGODB_CONFIG, db='third_open_plat', alias='third_open_plat')
connect(**MONGODB_CONFIG, db='cip_ops', alias='cip_ops')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")

SECRET_KEY = "dc393487a84ddf9da61fe0180ef295cf0642ecbc5d678a1589ef2e26b35fce9c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 43200  # 30天

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

deadline_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="The token has expired, Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_userList():
    qs = User.objects().values_list()
    return qs


res = get_userList()


def get_user(username: str):
    for user in res:
        if user.username == username:
            return user


def token_to_account(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username, expire = payload.get("sub"), payload.get("exp")
        user = get_user(username)
        if user is None:
            raise JWTError
        if time.time() > expire:
            raise deadline_exception
    except JWTError:
        raise credentials_exception
    return user


def create_token(data, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(
        claims=to_encode,
        key=SECRET_KEY,
        algorithm=ALGORITHM,
    )
