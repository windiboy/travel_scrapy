from peewee import *

# 连接数据库
database = MySQLDatabase('my_db', user='root', host='localhost', port=3306, password='yang0308')

class TravelContent(Model):
    id = IntegerField()
    source = IntegerField()
    user_name = CharField()
    key_words = CharField()
    title = CharField()
    content = TextField()
    province = CharField()
    status = IntegerField()
    travel_days = IntegerField()
    travel_spend = IntegerField()
    extra = TextField()
    publish_time = DateTimeField()
    departure_time = DateTimeField()
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        table_name = "travel_content"
        database = database