# -*- coding: utf-8 -*-

import time
from datetime import timedelta
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from app.endpoints.common.security_oauth import get_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_token, \
    credentials_exception
from configs.logging_set import logger


from fastapi.requests import Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

router = APIRouter(prefix="/api/third-party", tags=["安全登陆接口"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/third-party/token")



@router.post('/token', summary='1.1 获取身份凭证')
async def get_third_party_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    start_time = time.time()
    user = get_user(form_data.username)
    if not user or user.password != form_data.password:
        raise credentials_exception
    access_token = create_token(data={"sub": form_data.username},
                                expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    exp_time = int(time.time()) + ACCESS_TOKEN_EXPIRE_MINUTES * 60
    end_time = time.time()
    logger.info(
        f"request sucess. request_method--{request.method}   request_url--{request.url}  used_time--{end_time - start_time}s  request_boby--{form_data.username, form_data.password}")
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"code": 0, "msg": "success.", "access_token": access_token, "exp_time": exp_time, })



# 验证用户接口权限
def verifying_user_interface(path, username):
    Permission = UserInterfacePermission.objects.filter(username=username).first()
    if path in Permission.interface_url:
        return True
    else:
        return False


@router.post('/xx_lists', description='获取xx列表')
def get_vehicles(request: Request, oauth2: str = Depends(token_to_account)):
    """
    2.1获取xxx列表
    """
    # verify = verifying_user_interface(path=request.url.path, username=oauth2.username)

