from sqlalchemy.orm import Session
from db.models import AGENT
from schemas.agent import AgentCreate, AgentShow


def list_agents(db : Session):   
    agents = db.query(AGENT).all()
    return agents


def create_agent(agent: AgentCreate, db: Session):
    agent_object = AGENT(**agent.dict())
    db.add(agent_object)
    db.commit()
    db.refresh(agent_object)
    return agent_object


def retreive_agent(AGENT_CODE:str, db:Session):
    agent = db.query(AGENT).filter(AGENT.AGENT_CODE == AGENT_CODE).first()
    return agent


def update_agent(AGENT_CODE:str, agent: AgentShow, db: Session):
    existing_agent = db.query(AGENT).filter(AGENT.AGENT_CODE == AGENT_CODE)
    if not existing_agent.first():
        return 0
    existing_agent.update(agent.__dict__)
    db.commit()
    return 1


def delete_agent(AGENT_CODE:str, db: Session):
    existing_agent = db.query(AGENT).filter(AGENT.AGENT_CODE == AGENT_CODE)
    if not existing_agent.first():
        return 0
    existing_agent.delete(synchronize_session=False)
    db.commit()
    return 1