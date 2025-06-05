from fastapi import HTTPException,APIRouter,Depends
from src.models import *
from src.schemas import *
from sqlalchemy.orm import Session
from src.crud.agent_ticket import *
from src.database import get_db

agent_router_ticket=APIRouter(prefix="/agents")

@agent_router_ticket.post("/{id_agent}/tickets",response_model=AgentRead)
def add_ticket_to_agent(id_agent:int,id_ticket:int,db:Session=Depends(get_db)):
    agent=add_ticket(id_agent=id_agent,id_ticket=id_ticket,db=db)
    if not agent:
        return HTTPException(status_code=404,detail="Agent n'existe pas")
    return agent

@agent_router_ticket.delete("/{id_agent}/tickets/{id_ticket}",response_model=AgentRead)
def delete_ticket_from_agent(id_agent:int,id_ticket:int,db:Session=Depends(get_db)):
    agent=delete_ticket(id_agent=id_agent,id_ticket=id_ticket,db=db)
    if not agent:
        return HTTPException(status_code=404,detail="Agent n'existe pas")
    return agent

@agent_router_ticket.get("/{id_agent}/tickets",response_model=list[TicketSimple])
def get_all_ticket_from_agent(id_agent:int,db:Session=Depends(get_db)):
    tickets=get_tickets(id_agent=id_agent,db=db)
    if not tickets:
        raise HTTPException(status_code=404,detail="Aucun ticket")
    return tickets

@agent_router_ticket.get("/{id_agent}/tickets/{id_ticket}",response_model=TicketSimple)
def get_ticket_by_id(id_agent:int,id_tiket:int,db=Depends(get_db)):
    ticket=get_ticket(id_agent=id_agent,id_ticket=id_tiket,db=db)
    if not ticket:
        raise HTTPException(status_code=404,detail="Aucun ticket avec ce id")
    return ticket

@agent_router_ticket.put("/{id_agent}/tickets/{id_ticket}/statuts/{id_statut}",response_model=AgentRead)
def modify_statut_of_ticket(id_agent:int,id_ticket:int,id_statut:int,db:Session=Depends(get_db)):
    agent=modify_statut_ticket(id_agent=id_agent,id_ticket=id_ticket,id_new_statut=id_statut,db=db)
    if not agent:
        raise HTTPException(status_code=404,detail="Ticket not found")
    return agent

@agent_router_ticket.post("/{id_agent}/tickets/{id_categorie}/{motif}",response_model=AgentTicket)
def create_tiket_with_agent_and_categorie(motif:str,id_agent:int,id_categorie,db:Session=Depends(get_db)):
    create_agent_ticket_with_categorie_schema=AgentTicket(motif=motif,id_categorie=id_categorie,id_agent=id_agent)
    ticket_agent=add_ticket_to_agent_with_categorie(create_agent_ticket_with_categorie_schema,db=db)
    if not ticket_agent:
        raise HTTPException(status_code=404,detail="Aucun client ne correspond à lid passé")
    return ticket_agent
