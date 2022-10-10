from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from db.session import get_db
from typing import List 
from schemas.agent import AgentShow, AgentCreate
from db.repository.agent import list_agents, create_agent, retreive_agent, update_agent, delete_agent


router = APIRouter()


@router.get("/all", response_model=List[AgentShow])
def get_all_agents(db:Session = Depends(get_db)):
    agents = list_agents(db=db)
    return agents


@router.post("/create/",response_model=AgentShow)
def create_agents(agent: AgentCreate,db: Session = Depends(get_db)):
    agent = create_agent(agent=agent, db=db)
    return agent


@router.get("/agent/{agent_code}",response_model=AgentShow)
def read_agent(agent_code:str,db:Session = Depends(get_db)):
    agent = retreive_agent(AGENT_CODE=agent_code,db=db)
    if not agent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Agent with this id {agent_code} does not exist")
    return agent


@router.put("/update/{agent_code}") 
def update_agents(agent_code:str,agent: AgentCreate, db: Session = Depends(get_db)):
    message = update_agent(AGENT_CODE=agent_code,agent=agent,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Agent with id {agent_code} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{agent_code}")
def delete_agents(agent_code:str, db: Session = Depends(get_db)):
    agent = retreive_agent(AGENT_CODE=agent_code,db=db)
    if not agent:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Agent with this code {agent_code} does not exist")
    if agent:
        delete_agent(AGENT_CODE=agent_code,db=db)
        return {"detail": "Successfully deleted."} 
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")