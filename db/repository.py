from sqlalchemy.orm import Session
from db.models import AGENT


def list_agents(db : Session):   
    agents = db.query(AGENT).all()
    return agents