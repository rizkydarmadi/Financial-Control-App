from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,Float,Text
import json
from sqlalchemy.orm import sessionmaker

file = open('config.json')
config = json.load(file)

# database
database = config['database'][0]

username = database['user']
password = database['password']
host = database['host']
port = database['port']
database = database['name']

engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}",
        pool_size=20,
        max_overflow=0,
        pool_timeout=300,
    )

Session = sessionmaker(engine, future=True)

Base = declarative_base()

class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True, nullable=False)
    saldo = Column(Float)
    debit = Column(Float)
    credit = Column(Float)
    deskripsi = Column(Text)
    date = Column(DateTime(timezone=True))



