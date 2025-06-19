from fastapi import FastAPI
from src.routes.agent import agent_router
from src.routes.categorie import categorie_router
from src.routes.ticket import ticket_router
from src.routes.agent_ticket import agent_router_ticket
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"]
)

app.include_router(agent_router)
app.include_router(categorie_router)
app.include_router(ticket_router)
app.include_router(agent_router_ticket)