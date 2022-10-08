from typing import Optional
from pydantic import BaseModel



class AgentsBase(BaseModel):
    AGENT_CODE : Optional[str] = None
    AGENT_NAME : Optional[str] = None
    WORKING_AREA : Optional[str] = None
    COMMISSION : Optional[str] = None
    PHONE_NO : Optional[str] = None
    COUNTRY : Optional[str] = None


class ShowAgents(BaseModel):
    AGENT_CODE : Optional[str] = None
    WORKING_AREA : Optional[str] = None
    COMMISSION : Optional[str] = None
    PHONE_NO : Optional[str] = None

    class Config():
        orm_mode = True