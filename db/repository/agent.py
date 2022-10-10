from sqlalchemy.orm import Session
from db.models import AGENT
from schemas.agent import AgentCreate, AgentShow
import datetime, uuid



def list_agents(db : Session):   
    agents = db.query(AGENT).all()
    return agents


def create_agent(agent: AgentCreate, db: Session):
    create_at = str(datetime.datetime.now())
    agent_object = AGENT(
                        AGENT_CODE = agent.AGENT_CODE,
                        AGENT_NAME = agent.AGENT_NAME,
                        WORKING_AREA = agent.WORKING_AREA,
                        COMMISSION = agent.COMMISSION,
                        PHONE_NO = agent.PHONE_NO,
                        COUNTRY = agent.COUNTRY,
                        CREATE_AT = create_at,
    )
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