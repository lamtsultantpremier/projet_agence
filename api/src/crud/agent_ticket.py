from src.models import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import CreateEvenement,AgentTicket,TicketSimple
def add_ticket(id_agent:int,id_ticket:int,db:Session):
    agent=db.get(Agent,id_agent)
    if not agent:
        return None
    ticket=db.get(Ticket,id_ticket)
    if not ticket:
        return None
    agent.tickets.append(ticket)
    db.commit()
    db.refresh(agent)
    return agent

def delete_ticket(id_agent:int,id_ticket:int,db:Session):
    agent=db.get(Agent,id_agent)
    if not agent:
        return None
    ticket=db.get(Ticket,id_ticket)
    if not ticket:
        return None
    agent.tickets.remove(ticket)
    db.commit()
    return agent

def modify_statut_ticket(id_agent:int,id_ticket:int,id_new_statut:int,db:Session):
   agent=db.get(Agent,id_agent)
   if not agent:
       return None
   for ticket in agent.tickets:
       if ticket.id==id_ticket:
           ticket.id_statut=id_new_statut
           break
   modify_statut_of_ticket_by_his_id_for_all_agent(id_ticket=id_ticket,id_new_statut=id_new_statut,db=db)
   evenementschema=CreateEvenement(id_agent=id_agent,id_ticket=id_ticket,id_statut=id_new_statut)
   evenement=add_event(evenementschema,db)
   db.flush([agent,evenement])
   db.add(evenement)
   db.commit()
   db.refresh(agent)
   return agent

   
def get_tickets(id_agent:int,db:Session):
    agent=db.get(Agent,id_agent)
    if not agent:
        return None
    tickets=agent.tickets
    return tickets

def get_ticket(id_agent:int,id_ticket,db:Session):
    ticket_chosen=None
    agent=db.get(Agent,id_agent)
    if not agent:
        return None
    tickets=agent.tickets
    for ticket in tickets:
        if ticket.id==id_ticket:
            ticket_chosen=ticket
            break
    return ticket_chosen

def add_ticket_to_agent_with_categorie(create_agent_ticket_schema:AgentTicket,db:Session):
    agent=db.get(Agent,create_agent_ticket_schema.id_agent)
    if not agent:
        return None
    categorie=db.get(Categorie,create_agent_ticket_schema.id_categorie)
    if not categorie:
        return None
    create_agent_ticket_dict=create_agent_ticket_schema.model_dump()
    create_agent_ticket=Ticket(**create_agent_ticket_dict)
    create_agent_ticket.categorie=categorie
    db.add(create_agent_ticket)
    db.commit()
    db.refresh(create_agent_ticket)
    return create_agent_ticket

def send_tickets_agent_in_his_categorie(db:Session):
    agents=db.query(Agent).all()
    tickets=db.query(Ticket).all()
    for agent in agents:
        for ticket in tickets:
            if agent.id_categorie==ticket.id_categorie:
                agent.tickets.append(ticket)
    db.commit()
    return agents


def add_event(create_event:CreateEvenement,db:Session):
    evenement_dict=create_event.model_dump()
    evenement=Evenement(**evenement_dict)
    return evenement

def modify_statut_of_ticket_by_his_id_for_all_agent(id_ticket:int,new_id_statut:int,db:Session):
    ticket_in_db=db.get(Ticket,id_ticket)
    if not ticket:
        return None
    all_agent_in_the_same_category=db.scalars(select(Agent).where(Agent.id_categorie==ticket_in_db.id_categorie)).all()
    for agent in all_agent_in_the_same_category:
        for ticket in agent.tickets:
            if ticket.id==ticket_in_db.id:
                ticket.id_statut=new_id_statut
