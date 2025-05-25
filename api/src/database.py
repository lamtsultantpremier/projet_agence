from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass,sessionmaker,Session
from sqlalchemy import create_engine
import psycopg2

class Base(MappedAsDataclass,DeclarativeBase):
    pass

host="localhost"
username="postgres"
password="user"
port="5432"
database_name="gestion_client"
try:
    engine=create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}",echo=True)
    SessionLocal=sessionmaker(engine)
except Exception as e:
    print(f"Erreur = {e} {TypeError(e)}")

def get_db()->Session:
    db=SessionLocal()
    return db

