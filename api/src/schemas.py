from pydantic import BaseModel,EmailStr,ConfigDict,Field
from dataclasses import dataclass
from typing import Optional,List
from datetime import datetime
# Shema categorie
class CategorieBase(BaseModel):
    libelle:str   

class CreateCategorie(CategorieBase):
    pass

class ReadCategorie(CategorieBase):
    id:int
    model_config=ConfigDict(from_attributes=True)



# Schema statut
class TicketSimple(BaseModel):
    id:int
    motif:str
    id_statut:int
    id_categorie:int
    model_config=ConfigDict(from_attributes=True)

class StatutBase(BaseModel):
    libelle:str

class CreateStatut(StatutBase):
    pass

class ReadStatut(StatutBase):
   id:int
   tickets:'List[TicketSimple]'=Field(default_factory=list)

   model_config=ConfigDict(from_attributes=True)


# Schema Ticket
class AgentSimple(BaseModel):
    nom:str
    prenom:str
    telephone:str
    email:EmailStr
    model_config=ConfigDict(from_attributes=True)

class TicketBase(BaseModel):
    motif:str
    id_categorie:int

class CreateTicket(TicketBase):
    pass

class ReadTicket(TicketBase):
    id:int
    id_statut:int
    agents:'Optional[List[AgentCreate]]'=Field(default_factory=list)
    model_config=ConfigDict(from_attributes=True)

class AgentTicket(CreateTicket):
    id_agent:int
    model_config=ConfigDict(from_attributes=True)
# Schema Agent

class AgentBase(BaseModel):
    nom:str
    prenom:str
    telephone:str
    email:EmailStr
    id_categorie:int

class AgentCreate(AgentBase):
    pass

class AgentRead(AgentBase):
    id_agent:int
    id_categorie:int
    tickets:List[TicketSimple]=Field(default_factory=list)
    model_config=ConfigDict(from_attributes=True)


class AgentUpate(BaseModel):
    nom:Optional[str]=None
    prenom:Optional[str]=None
    telephone:Optional[str]=None
    email:Optional[EmailStr]=None
    id_categorie:int
    

class EvenementBase(BaseModel):
    id_agent:int
    id_ticket:int
    id_statut:int
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
