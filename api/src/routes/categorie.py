from fastapi import APIRouter
from src.schemas import CreateCategorie,ReadCategorie
from sqlalchemy.orm import Session
from src.database import get_db
from fastapi import Depends
from fastapi import HTTPException
from src.crud.categorie import *
categorie_router=APIRouter(prefix="/categories")

@categorie_router.post("/")
def create_categorie(categorie:CreateCategorie,db:Session=Depends(get_db)):
    id=create_catgorie(categorie=categorie,db=db)
    return {"message":id}

@categorie_router.get("/{id_categorie}",response_model=ReadCategorie)
def get_categorie_by_id(id_categorie:int,db:Session=Depends(get_db)):
    categorie=read_categorie(db=db,id_categorie=id_categorie)
    if not categorie:
        raise HTTPException(status_code=404,detail="Categorie nom trouvée")
    return categorie

@categorie_router.get("",response_model=list[ReadCategorie])
def get_all_categorie(db:Session=Depends(get_db)):
    all_categories=read_categories(db=db)
    return all_categories

@categorie_router.delete("/{id_categorie}")
def delete_categorie_data(id_categorie:int,db:Session=Depends(get_db)):
    id=delete_categorie(id_categorie=id_categorie,db=db)
    if not id:
        raise HTTPException(status_code=404,detail="La categorie n'existe pas")
    else:
        return {"id",id}
