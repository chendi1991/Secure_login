# Secure_login
`安全登陆接口服务`

以下有关面试问题:
# 1.安全性

采用fastapi-OAuth2  多种授权模式,本demo采用授权码模式
客户端必须得到用户的授权，才能获得令牌（access token）
POST /token HTTP/1.1  #指定路由
Host: server.example.com   #可以规定IP主机访问
Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW  #认证密钥
Content-Type: application/x-www-form-urlencoded  #请求头类型
获取令牌后，开放接口都依赖token,具有时效性

# 2.注意选择的技术栈，说明为什么这样选择

安全登陆接口使用框架 Fastapi+OAuth2+mongoengine
使用原因:
(1）fastapi快速构后端接口 ，包括依赖项，安全组件、数据库的集成、中间件等 
（2）OAuth2处理身份认证和授权，自定义密钥规范 bearer token等
（3）mongoengine orm model模型的使用

# 3.注意权限验证的便捷性，使得其他地方也能使用
我在配置项中定义了权限验证的create_token函数,具体现configs/security_oauth.py
在接口定义中 验证权限token_to_account,具体现app/endpoints/common/security_oauth.py


# 4.考虑性能、可扩展性，说明如何达到的
FastAPI 快速高性能的web框架，归功于Starlette
（1）支持异步  比如： async def get_third_party_token()
 (2)Starlette基于ASGI标准实现的,asyncio 库来实现非阻塞的网络 I/O
(3)可以灵活配置服务端的ip，port等，包括请求段的请求头验证
（4）支持多样式部署，单机supervise及docker部署方式


# 项目树
├── app    
│   ├── endpoints
│   │   ├── cloud_server.py   #业务层
│   │   ├── common    #通用业务层
│   │   │   ├── security_oauth.py  #安全
│   │   │   ├── user_permission.py  #用户
│   │   │   └── __init__.py 
│   │   └── __init__.py 
│   └── __init__.py 
├── asgi.py    # docker部署初始化入口
├── configs    # 配置文件 日志 通用参数等
│   ├── logging_set.py 
│   ├── security_oauth.py 
│   ├── setting.py
│   └── __init__.py
├── Dockerfile   #dockerfile
├── docs
├── logs        #日志
│   └── __init__.py 
├── main.py    #调试入口
├── models     #对象模型
│   ├── models.py 
│   └── __init__.py 
├── README.md   
├── requirements.txt  #python 依赖（docker构建需要）
├── static    #openapi本地调试文件
│   ├── swagger-ui-bundle.js 
│   ├── swagger-ui.css 
│   └── __init__.py 
└── utils    #工具
 


## 1. 身份鉴权接口文档说明

### 1.1 获取身份凭证

```
POST http://{{host}}:{{port}}/api/third-party/token
```

- request body

```json
{
	"username": "1", //应用id
    "password": "1" //应用秘钥
}
```

- response body

```json
{
    "code": 0,
    "data": {
    	"token": "xxxxxxxx", //身份凭证
        "exp_time": 1641818622, //过期时间 10位或13位时间戳 
    },
    "msg": "success"
}
```

注：后续接头请求报文头，携带Token。

- request headers

```
Authorization: token //token通过获取身份凭证接口获得
```

