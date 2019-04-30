from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,create_engine
from sqlalchemy.types import CHAR,Integer,String,Text
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://lynxi:lynxi@localhost:5432/test')

Base = declarative_base()


class User(Base):
    __tablename__ = 't_user'
    userid = Column('userid',Integer,primary_key=True,nullable=True)
    username = Column('username',String(64),nullable=True)
    password = Column('password',String(64),nullable=True)


User.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)

session = DBsession()
query = session.query(User)

print(query)

print(engine)


