# 版本切换
SWITCH_VERSION = True

# 初始主机
INIT_HOST = "127.0.0.1"

# 初始端口
INIT_PORT = 8888


try:
    from .local_setting import *
except ImportError as e:
    print(f"local_cloud_server ImportError, exc:{e}")
