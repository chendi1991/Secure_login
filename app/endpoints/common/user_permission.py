from pymongo import MongoClient

from models.models import UserPermission

from configs.setting import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASSWORD


def verifying_user_interface(path, username):
    """
    验证用户接口权限
    """
    Permission = UserPermission.objects.filter(username=username).first()
    if path in Permission.interface_url:
        return True
    else:
        return False


def verifying_user_vehicles(username, vehicles):
    """
    验证用户车辆权限
    """
    qs = UserPermission.objects.filter(username=username).first()
    if vehicles is None:
        return qs.vehicles
    else:
        intersection_vehicles = list(set(qs.vehicles).intersection(set(vehicles)))
        return intersection_vehicles


def pymongo_connect():
    """
    pymongo连接
    """
    client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    client.admin.authenticate(f"{MONGO_USERNAME}", f"{MONGO_PASSWORD}")
    return client
