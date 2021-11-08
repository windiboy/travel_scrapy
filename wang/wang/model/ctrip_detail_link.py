from peewee import *

# 连接数据库
database = MySQLDatabase('my_db', user='root', host='localhost', port=3306, password='yang0308')

class CtripDetailLink(Model):
    id = IntegerField()
    name = CharField()
    content = CharField()
    status = IntegerField()
    extra = TextField()
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        table_name = "ctrip_detail_link"
        database = database