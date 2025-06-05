from fastapi import APIRouter,HTTPException
from src.schemas import CreateTicket,ReadTicket
from sqlalchemy.orm import Session
from src.database import get_db
from src.crud.ticket import *
from fastapi import Depends
ticket_router=APIRouter(prefix="/tickets")

@ticket_router.post("")
def create_tickets(ticket:CreateTicket,db:Session=Depends(get_db)):
    id_ticket=create_ticket(ticket=ticket,db=db)
    return{"id ticket":id_ticket}

@ticket_router.get("/{id_ticket}",response_model=ReadTicket)
def read_ticket_by_id(id_ticket:int,db:Session=Depends(get_db)):
    ticket=read_ticket(id_tiket=id_ticket,db=db)
    if not ticket:
        raise HTTPException(status_code=404,detail="le ticket n'existe pas")
    return ticket

@ticket_router.delete("/{id_ticket}")
def delete_ticket_by_id(id_ticket:int,db:Session=Depends(get_db)):
    id_ticket=delete_ticket(id_ticket=id_ticket,db=db)
    return{"id":id_ticket}

@ticket_router.get("",response_model=list[ReadTicket])
def get_all_tickets(db:Session=Depends(get_db)):
    tickets=get_tickets(db=db)
    if not tickets:
        raise HTTPException(status_code=404,detail="Aucun ticket trouvé")
    return tickets

@ticket_router.get("/categories/{id_categorie}",response_model=list[ReadTicket])
def get_tickets_for_his_categorie(id_categorie:int,db:Session=Depends(get_db)):
    tickets=get_ticket_by_categorie(id_categorie=id_categorie,db=db)
    if not tickets:
        raise HTTPException(status_code=404,detail="Aucun ticket avec cette categorie")
    return tickets
@ticket_router.get("/statuts/{id_statut}",response_model=list[ReadTicket])
def get_tickets_by_his_statut(id_statut:int,db:Session=Depends(get_db)):
    tickets=get_ticket_by_statut(id_statut=id_statut,db=db)
    if not tickets:
        raise HTTPException(status_code=404,detail="Aucun ticket dans cette categorie")
    return tickets


@ticket_router.put("/{id_ticket}/categories/{id_new_categorie}",response_model=ReadTicket)
def change_ticket_categorie(id_ticket:int,id_new_categorie:int,db:Session=Depends(get_db)):
    tickets=change_categorie(id_new_categorie=id_new_categorie,id_ticket=id_ticket,db=db)
    if not tickets:
        raise HTTPException(status_code=404,detail="Aucun Tickets pour cette Categorie")
    return tickets

@ticket_router.put("/{id_ticket}/statuts/{id_new_statut}",response_model=ReadTicket)
def change_ticket_statut(id_ticket:int,id_new_statut:int,db:Session=Depends(get_db)):
    ticket=change_statut(id_ticket=id_ticket,id_new_statut=id_new_statut,db=db)
    if not ticket:
        raise HTTPException(status_code=404,detail="Veuillez renseigner correctement")
    return ticket

@ticket_router.put("/{id_ticket}/agents/{id_agent}")
def add_ticket_to_agent(id_ticket:int,id_agent:int,db:Session=Depends(get_db)):
    id_agent=assign_ticket_to_agent(id_ticket=id_ticket,id_agent=id_agent,db=db)
    return id_agent
