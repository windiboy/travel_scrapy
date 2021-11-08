from peewee import *

# 连接数据库
database = MySQLDatabase('my_db', user='root', host='localhost', port=3306, password='yang0308')

class MfwDetailLink(Model):
    id = IntegerField()
    link_id = IntegerField()
    content = TextField()
    status = IntegerField()
    extra = TextField()
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        table_name = "mfw_detail_link"
        database = database