import logging
import os
import time


def mylogger():
    """
    设置LOGGING参数
    """
    # 实例化logger对象,设置日志登记为DEBUG
    logger_obj = logging.getLogger(__name__)
    logger_obj.setLevel(level=logging.DEBUG)

    # Formatter
    formatter = logging.Formatter(fmt='%(asctime)s  - %(levelname)s - %(message)s -%(filename)s %(funcName)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    # 设置logger路径
    rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_path = os.path.join(os.path.dirname(os.path.abspath("__dir__")), 'logs/')
    log_name = log_path + rq + '.log'

    # handler处理器
    handler = logging.FileHandler(log_name)
    logger_obj.addHandler(handler)
    rf_handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger_obj.addHandler(rf_handler)
    return logger_obj


logger = mylogger()

