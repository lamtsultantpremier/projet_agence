from src.schemas import CreateTicket
from src.database import Session
from src.models import Ticket,Evenement
from src.models import Categorie,Agent,Statut
from src.schemas import TicketSimple,CreateEvenement
from sqlalchemy import select,event

def create_ticket(ticket:CreateTicket,db:Session):
    ticket_dict=ticket.model_dump()
    ticket=Ticket(**ticket_dict)
    categorie=db.get(Categorie,ticket_dict["id_categorie"])
    ticket.categorie=categorie
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket.id

def read_ticket(id_tiket:int,db:Session):
    ticket=db.get(Ticket,id_tiket)
    if not ticket:
        return None
    return ticket

def delete_ticket(id_ticket:int,db:Session):
    ticket=db.get(Ticket,id_ticket)
    if not ticket:
        return None
    db.delete(ticket)
    db.commit()
    return ticket.id

def change_categorie(id_new_categorie:int,id_ticket:int,db:Session):
    ticket=db.get(Ticket,id_ticket)
    categorie=db.get(Categorie,id_new_categorie)
    ticket.categorie=categorie
    db.commit()
    db.refresh(ticket)
    return ticket

def change_statut(id_ticket:int,id_new_statut:int,db:Session):
    ticket=db.get(Ticket,id_ticket)
    if not ticket:
        return None
    statut=db.get(Statut,id_new_statut)
    if not statut:
        return None
    ticket.statut=statut
    db.commit()
    db.refresh(ticket)
    return ticket

def get_tickets(db:Session):
    tickets=db.query(Ticket).all()
    if not tickets:
        return None
    return tickets

def get_ticket_by_categorie(id_categorie:int,db:Session):
    #tickets=db.scalars(select(Ticket).where(Ticket.id_categorie==id_categorie)).all()
    tickets=db.query(Ticket).filter_by(id_categorie=id_categorie).all()
    if not tickets:
        return None
    return tickets

def get_ticket_by_statut(id_statut:int,db:Session):
    tickets=db.scalars(select(Ticket).where(Ticket.id_statut==id_statut)).all()
    if not tickets:
        return None
    return tickets


# def assign_ticket_to_agent(id_categorie:int,ticket:Ticket,db:Session):
#     all_agents=db.scalars(select(Agent).where(Agent.id_categorie==id_categorie)).all()
#     for agent in all_agents:
#         agent.tickets.append(ticket)

def assign_ticket_to_agent(id_ticket:int,id_agent:int,db:Session):
    agent=db.get(Agent,id_agent)
    ticket=db.get(Ticket,id_ticket)
    ticket.id_agent=agent.id_agent
    #Ajoute un evenement qui permet de savoir quel agent est en charge de tel ticket 
    create_event(id_ticket=ticket.id,id_agent=agent.id_agent,id_statut=ticket.id_statut,db=db)
    db.commit()
    db.refresh(ticket)
    return ticket.id_agent

def create_event(id_ticket:int,id_agent:int,id_statut:int,db:Session):
    evenement_dict=CreateEvenement(id_agent=id_agent,id_ticket=id_ticket,id_statut=id_statut).model_dump()
    evenement=Evenement(**evenement_dict)
    db.add(evenement)
    db.commit()




