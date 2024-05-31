from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

URL_Database = 'postgresql://postgres:Reaper@localhost:5432/user_data'

engine = create_engine(URL_Database)
Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)

class Companys(Base):
    __tablename__='datas'
    id=Column(Integer,primary_key=True,index=True)
    company_name=Column(String)
    company_details=Column(String)



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

