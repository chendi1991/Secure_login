import datetime

from mongoengine import *


class UserPermission(Document):
    username = StringField(hlep_text='用户名')
    interfaces = ListField(hlep_text='接口权限列表')
    vehicles = ListField(title='车辆权限列表')
    update_time = DateTimeField(required=True, title="更新时间", default=datetime.datetime.now())
    create_time = DateTimeField(required=True, title="创建时间", default=datetime.datetime.now())
    description = StringField(title="描述信息")
    meta = {'db_alias': 'third_open_plat', "collection": "user_permission"}


class User(Document):
    username = StringField(required=True, title='账户')
    password = StringField(required=True, title='密码')
    create_time = DateTimeField(required=True, title='创建日期', default=datetime.datetime.now())
    update_time = DateTimeField(required=True, title='更新日期', default=datetime.datetime.now())
    meta = {'db_alias': 'third_open_plat', "collection": "user"}

