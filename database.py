from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


engine=create_engine("postgresql://mestum:200796parviz@localhost/mestumplayer", echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)