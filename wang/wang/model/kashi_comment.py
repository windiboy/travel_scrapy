from peewee import *

# 连接数据库
database = MySQLDatabase('my_db', user='root', host='localhost', port=3306, password='yang0308')

class KashiComment(Model):
    id = IntegerField()
    user_name = CharField()
    content = TextField()
    status = IntegerField()
    star = IntegerField()
    extra = TextField()
    publish_time = DateTimeField()
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        table_name = "kashi_comment"
        database = database