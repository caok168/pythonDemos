from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,create_engine
from sqlalchemy.types import CHAR,Integer,String,Text,DateTime
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('postgresql://lynxi:lynxi@localhost:5432/test')

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(64), nullable=True)
    ip = Column('ip', String(64), nullable=True)
    address = Column('address', String(64), nullable=True)
    url = Column('url', String(64), nullable=True)
    vendor = Column('vendor', String(64), nullable=True)
    deviceModel = Column('device_model', String(64), nullable=True)
    accessProtocol = Column('access_protocol', String(64), nullable=True)
    transportProtocol = Column('transport_protocol', String(64), nullable=True)
    remark = Column('remark', String(64), nullable=True)
    createdAt = Column('created_at', DateTime, nullable=False, default=datetime.datetime.now, comment='创建时间')
    modifiedAt = Column('modified_at', DateTime, nullable=False, default=datetime.datetime.now, comment='修改时间')
    deletedAt = Column('deleted_at', DateTime, nullable=True)


Device.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class DeviceOpeartor:

    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = Device(name='摄像头',ip='192.168.8.12')
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(Device).get(1)

    def get_all(self):
        return self.session.query(Device).filter_by(name='摄像头')

    def update(self, pk):
        new_obj = self.session.query(Device).get(pk)

        if new_obj:
            new_obj.name = 'test'
            new_obj.url ='www.baidu.com'
            new_obj.modifiedAt = datetime.datetime.now()
            # self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def delete(self, pk):
        # 删除数据
        new_obj = self.session.query(Device).get(pk)
        self.session.delete(new_obj)
        self.session.commit()


device = DeviceOpeartor()
# res = device.add_one()
# print(res)
res = device.get_one()
print(res)

isok = device.update(3)
print(isok)


# device.delete(1)