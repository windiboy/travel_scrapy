from peewee import *

# 连接数据库
database = MySQLDatabase('my_db', user='root', host='localhost', port=3306, password='yang0308')

class ChaoyangParkComment(Model):
    id = IntegerField()
    user_name = CharField()
    content = TextField()
    status = IntegerField()
    source = IntegerField()
    star = IntegerField()
    extra = TextField()
    publish_time = DateTimeField()
    create_time = DateTimeField()
    modify_time = DateTimeField()
    park_name = CharField()

    class Meta:
        table_name = "chaoyang_park_comment"
        database = database