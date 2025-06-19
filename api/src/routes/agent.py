from fastapi import APIRouter
from src.schemas import AgentCreate,AgentRead,AgentUpate,TicketSimple
from src.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from src.crud.agent import create_agent,get_agents,update_agent,delete_agent,get_agent

agent_router=APIRouter(prefix="/agents")

@agent_router.post("")
def create_agents(agent:AgentCreate,db:Session=Depends(get_db)):
    id_agent=create_agent(db=db,agent_create=agent)
    return {"id":id_agent}

@agent_router.get("/",response_model=list[AgentRead])
def get_all_agent(db:Session=Depends(get_db)):
    agents=get_agents(db=db)
    return agents

@agent_router.get("/{id_agent}",response_model=AgentRead)
def get_agent_by_id(id_agent:int,db:Session=Depends(get_db)):
    agent=get_agent(id_agent=id_agent,db=db)
    if not agent:
        raise HTTPException(status_code=404,detail="l'Agent n'existe pas")
    return agent

@agent_router.put("/{id_agent}")
def modify_agent_data(id_agent:int,agent_update:AgentUpate,db:Session=Depends(get_db)):
    id_agent_modify=update_agent(db=db,agent_id=id_agent,agent_update=agent_update)
    return {"message":id_agent}

@agent_router.delete("/{id_agent}")
def delete_agent_data(id_agent:int,db:Session=Depends(get_db)):
    id_deleted=delete_agent(db=db,id_agent=id_agent)
    return {"message":id_deleted}


