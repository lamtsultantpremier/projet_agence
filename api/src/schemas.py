from pydantic import BaseModel,EmailStr,ConfigDict
from dataclasses import dataclass
from typing import Optional,List
from datetime import datetime

class CategorieBase(BaseModel):
    libelle:str   

class CreateCategorie(CategorieBase):
    pass

class ReadCategorie(CategorieBase):
    id:int
    model_config=ConfigDict(from_attributes=True)

class StatutBase(BaseModel):
    libelle:str

class CreateStatut(StatutBase):
    pass

class ReadStatut(StatutBase):
   id:int
   tickets:'List[ReadTicket]'=[]

   model_config=ConfigDict(from_attributes=True)

class TicketBase(BaseModel):
    motif:str
    id_categorie:int

class CreateTicket(TicketBase):
    pass

class ReadTicket(TicketBase):
    id:int
    agents:'List[AgentRead]'=[]

    model_config=ConfigDict(from_attributes=True)

class AgentBase(BaseModel):
    nom:str
    prenom:str
    telephone:str
    email:EmailStr
    id_categorie:int

class AgentCreate(AgentBase):
    pass

class AgentRead(AgentBase):
    id:int
    tickets:List[ReadTicket]=[]

    model_config=ConfigDict(from_attributes=True)


class AgentUpate(BaseModel):
    nom:Optional[str]=None
    prenom:Optional[str]=None
    telephone:Optional[str]=None
    email:Optional[EmailStr]=None
    

class EvenementBase(BaseModel):
    id_agent:int
    id_ticket:int
class CreateEvenement(EvenementBase):
    pass


class ReadEvenement(EvenementBase):
   id:int
   date_enregistrement:datetime

   model_config=ConfigDict(from_attributes=True)

ReadCategorie.model_rebuild()
ReadStatut.model_rebuild()
ReadTicket.model_rebuild()
AgentRead.model_rebuild()
ReadEvenement.model_rebuild()
