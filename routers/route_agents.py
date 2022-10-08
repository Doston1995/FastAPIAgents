from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db
from typing import List 
from db.schemas import ShowAgents
from db.repository import list_agents
router = APIRouter()


@router.get("/all", response_model=List[ShowAgents])
def get_all_agents(db:Session = Depends(get_db)):
    agents = list_agents(db=db)
    return agents