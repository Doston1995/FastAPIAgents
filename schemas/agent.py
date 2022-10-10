from datetime import date
from typing import Optional, List
from pydantic import BaseModel



class AgentBase(BaseModel):
    AGENT_CODE : Optional[str] = None
    AGENT_NAME : Optional[str] = None
    WORKING_AREA : Optional[str] = None
    COMMISSION : Optional[str] = None
    PHONE_NO : Optional[str] = None
    COUNTRY : Optional[str] = None


class AgentCreate(BaseModel):
    AGENT_CODE : str
    AGENT_NAME : str
    WORKING_AREA : str
    COMMISSION : str
    PHONE_NO : str
    COUNTRY : str


class AgentShow(BaseModel):
    AGENT_CODE : str
    WORKING_AREA : str
    COMMISSION : str
    PHONE_NO : str

    class Config():
        orm_mode = True