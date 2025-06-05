"""Define all crud methodes"""
from src.schemas import CreateCategorie,ReadCategorie
from src.models import Categorie
from src.database import get_db
from sqlalchemy.orm import Session
#create categorie

def create_catgorie(categorie:CreateCategorie,db:Session):
    categorie_dict=categorie.model_dump()
    categorie=Categorie(**categorie_dict)
    db.add(categorie)
    db.commit()
    db.refresh(categorie)
    return categorie.id

def read_categorie(db:Session,id_categorie:int):
    categorie=db.query(Categorie).get(id_categorie)
    return categorie

def read_categories(db:Session):
    all_categories=db.query(Categorie).all()
    return all_categories

def delete_categorie(db:Session,id_categorie:int):
    categorie=db.get(Categorie,id_categorie)
    if not categorie:
        return None
    else:
        db.delete(categorie)
        db.commit()
        return categorie.id