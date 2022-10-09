from typing import Optional, List
from pydantic import BaseModel


######################## Agents #####################################
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


######################## Customers #####################################

class CustomerBase(BaseModel):
    CUST_CODE : Optional[str] = None
    CUST_NAME : Optional[str] = None
    CUST_CITY: Optional[str] = None
    WORKING_AREA : Optional[str] = None
    CUST_COUNTRY : Optional[str] = None
    GRADE : int
    OPENING_AMT : Optional[str] = None
    RECEIVE_AMT : Optional[str] = None
    PAYMENT_AMT : Optional[str] = None
    OUTSTANDING_AMT : Optional[str] = None
    PHONE_NO : Optional[str] = None
    AGENT_CODE : Optional[str] = None


class CustomerCreate(BaseModel):
    CUST_CODE : str
    CUST_NAME : str
    CUST_CITY: str
    WORKING_AREA : str
    CUST_COUNTRY : str
    GRADE : int
    OPENING_AMT : str
    RECEIVE_AMT : str
    PAYMENT_AMT : str
    OUTSTANDING_AMT : str
    PHONE_NO : str
    AGENT_CODE : Optional[str]


class CustomerShow(BaseModel):
    CUST_CODE : str
    WORKING_AREA : str
    GRADE : int
    OPENING_AMT : str
    RECEIVE_AMT : str
    PAYMENT_AMT : str
    OUTSTANDING_AMT : str
    AGENT_CODE : Optional[str]
    
    class Config():
        orm_mode = True
        
        
######################## Orders #####################################