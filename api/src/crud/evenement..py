from schemas import CreateEvenement,ReadEvenement
from sqlalchemy.orm import Session
from models import *

def create_evenement(evenement_create:CreateEvenement,db:Session):
    evenement_dict=evenement_create.model_dump()
    evenement=Evenement(**evenement_dict)
    db.add(evenement)
    db.commit()
    db.refresh(evenement)
    return evenement


