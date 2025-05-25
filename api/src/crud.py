from src.models import *
from sqlalchemy.orm import Session
from src.schemas import *
#Crud file
#agent function crud
def create_agent(db:Session,agent_create:AgentCreate)->int:
    agent_create_dict=agent_create.model_dump()
    categorie=db.get(Categorie,agent_create.model_dump()["id_categorie"])
    agent=Agent(**agent_create_dict)
    agent.categorie=categorie
    #envoie l'instruction d'insertion à la base de donnée sans faire l'insertion
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent.id_agent

def get_agents(db:Session):
    all_users=db.query(Agent).all()
    return all_users

def delete_agent(db:Session,id_agent:int)->int:
    agent=db.query(Agent).get(id_agent)
    db.delete(agent)
    db.commit()
    return agent.id_agent

def update_agent(db:Session,agent_id:int,agent_update:AgentUpate)->int:
    agent_in_database=db.get(Agent,agent_id)
    
    for field,value in agent_update.model_dump(exclude_unset=True).items():
        setattr(agent_in_database,field,value)
    db.commit()
    db.refresh(agent_in_database)
    return agent_in_database.id_agent
    