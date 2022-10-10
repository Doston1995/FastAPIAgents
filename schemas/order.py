from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class OrderBase(BaseModel):
    ORD_NUM : Optional[str] = None
    ORD_AMOUNT : Optional[str] = None
    ADVANCE_AMOUNT : Optional[date] = None
    ORD_DATE : Optional[date] = None
    CUST_CODE : Optional[str] = None
    AGENT_CODE : Optional[str] = None
    ORD_DESCRIPTION : Optional[str] = None


class OrderCreate(BaseModel):
    ORD_NUM : str
    ORD_AMOUNT : str
    ADVANCE_AMOUNT : str
    ORD_DATE : date
    CUST_CODE : str
    AGENT_CODE : str
    ORD_DESCRIPTION : str

    class Config():
        orm_mode = True

class OrderShow(BaseModel):
    ORD_NUM : str
    ORD_AMOUNT : str
    ADVANCE_AMOUNT : str
    ORD_DATE : date
    CUST_CODE : str
    AGENT_CODE : str
    ORD_DESCRIPTION : str

    class Config():
        orm_mode = True