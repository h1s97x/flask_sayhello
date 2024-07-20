from faker import Faker

from app.extensions import db
from app.models import Message

fake = Faker()

def fake_message(count=50):
    # 循环 count 次，生成假消息
    for i in range(count):
        message = Message(
            # 生成随机姓名
            name=fake.name(),
            # 生成随机句子
            body=fake.sentence(),
            # 生成今年内的随机日期时间
            timestamp=fake.date_time_this_year()
        )
        # 将生成的假消息添加到数据库会话中
        db.session.add(message)

    # 提交数据库会话，将假消息保存到数据库中
    db.session.commit()