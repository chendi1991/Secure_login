# Secure_login
`安全登陆接口服务`

安全登陆接口使用框架 Fastapi+OAuth2+mongoengine
使用原因:
1.fastapi快速构后端接口 ，包括依赖项，安全组件、数据库的集成、中间件等
2.OAuth2处理身份认证和授权，自定义密钥规范 bearer token等
3.mongoengine orm model模型的使用



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
 


## 1. 身份鉴权

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

