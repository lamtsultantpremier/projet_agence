from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column,relationship
from sqlalchemy import String,ForeignKey,Table,DateTime,func
from dataclasses import dataclass
from typing import List,Optional
from datetime import datetime

class Base(MappedAsDataclass,DeclarativeBase):
    pass

class Categorie(Base):
    __tablename__="categorie"
    id:Mapped[int]=mapped_column(name="id_categorie",primary_key=True,autoincrement=True,init=False)
    libelle:Mapped[str]=mapped_column(String(30),name="libelle_categorie")
    agents:Mapped[Optional[List["Agent"]]]=relationship(back_populates="categorie",default_factory=list)
    tickets:Mapped[Optional[List["Ticket"]]]=relationship(back_populates="categorie",default_factory=list)
    
class Statut(Base):
    __tablename__="statut"
    id:Mapped[int]=mapped_column(name="id_statut",init=False,primary_key=True,autoincrement=True)
    libelle:Mapped[str]=mapped_column(String(30),name="libelle_statut")
    tickets:Mapped[Optional[List["Ticket"]]]=relationship(back_populates="statut",default_factory=list)


class Agent(Base):
    __tablename__="agent"
    id_agent:Mapped[int]=mapped_column(name="id_agent",init=False,primary_key=True,autoincrement=True)
    id_categorie:Mapped[int]=mapped_column(ForeignKey("categorie.id_categorie"))
    nom:Mapped[str]=mapped_column(String(50),name="nom_agent")
    prenom:Mapped[str]=mapped_column(String(50),name="prenom_agent")
    telephone:Mapped[str]=mapped_column(String(20),name="telephone_agent")
    email:Mapped[str]=mapped_column(String(50),name="email_agent")
    categorie:Mapped[Optional["Categorie"]]=relationship(back_populates="agents",default=None)
    tickets:Mapped[Optional[List["Ticket"]]]=relationship(back_populates="agents",secondary="evenement",default_factory=list)

class Ticket(Base):
    __tablename__="ticket"
    id:Mapped[int]=mapped_column(name="id_ticket",primary_key=True,autoincrement=True,init=False)
    motif:Mapped[str]=mapped_column(String(50),name="motif_ticket")
    id_categorie:Mapped[int]=mapped_column(ForeignKey("categorie.id_categorie"),nullable=True)
    id_agent:Mapped[Optional[int]]=mapped_column(ForeignKey("agent.id_agent"),nullable=True,default=None)
    id_statut:Mapped[Optional[int]]=mapped_column(ForeignKey("statut.id_statut"),nullable=True,default=1)
    categorie:Mapped[Optional["Categorie"]]=relationship(back_populates="tickets",default=None)
    statut:Mapped[Optional["Statut"]]=relationship(back_populates="tickets",default=None)
    agents:Mapped[Optional[List["Agent"]]]=relationship(back_populates="tickets",secondary="evenement",default_factory=list)

class Evenement(Base):
    __tablename__="evenement"
    id:Mapped[int]=mapped_column(name="id_evenement",primary_key=True,autoincrement=True,init=False)
    id_agent:Mapped[int]=mapped_column(ForeignKey("agent.id_agent"))
    id_ticket:Mapped[int]=mapped_column(ForeignKey("ticket.id_ticket"))
    date_enregistrement:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),name="created_at")


    