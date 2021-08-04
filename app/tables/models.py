import datetime
#from uuid import uuid4
from sqlalchemy import DateTime, Column, Integer, String
from app import db

class Target(db.Model):

    __tablename__ = 'Target'

    #uuid = Column(String(36), primary_key=True, unique=True, nullable=False, default=lambda: str(uuid4()), comment='uuid')
    id = Column(Integer, primary_key=True, autoincrement=True, comment='target_id')
    ip = Column(String(46), nullable=False, unique=True, comment='ip地址')
    status = Column(String(4), default="down", comment='ip地址')
    flag_number = Column(Integer,default=0,comment="flag数")
    create_time = Column(DateTime, default=datetime.datetime.now, comment='修改时间')

    def __repr__(self):
        return str(self.ip)


