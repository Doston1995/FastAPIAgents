from sqlalchemy import CHAR, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class AGENT(Base):
    __tablename__ = 'AGENTS'

    AGENT_CODE   = Column(String(6), primary_key=True)
    AGENT_NAME   = Column(String(40))
    WORKING_AREA = Column(String(35))
    COMMISSION   = Column(String(10))
    PHONE_NO     = Column(String(15))
    COUNTRY      = Column(String(25))
    CREATE_AT    = Column(String(50))


class User(Base):
    
    __tablename__ = 'users'

    id         = Column(String, primary_key=True)
    username   = Column(String)
    password   = Column(String)
    first_name = Column(String)
    last_name  = Column(String)
    gender     = Column(String)
    create_at  = Column(String)
    status     = Column(CHAR(1))


class CUSTOMER(Base):
    __tablename__ = 'CUSTOMER'
    
    CUST_CODE       = Column(String(6), primary_key=True)
    CUST_NAME       = Column(String(40), nullable=False)
    CUST_CITY       = Column(String(35))
    WORKING_AREA    = Column(String(35), nullable=False)
    CUST_COUNTRY    = Column(String(20), nullable=False)
    GRADE           = Column(Integer)
    OPENING_AMT     = Column(CHAR(12), nullable=False)
    RECEIVE_AMT     = Column(CHAR(12), nullable=False)
    PAYMENT_AMT     = Column(CHAR(12), nullable=False)
    OUTSTANDING_AMT = Column(CHAR(12), nullable=False)
    PHONE_NO        = Column(String(17), nullable=False)
    CREATE_AT       = Column(String(50))
    AGENT_CODE      = Column(ForeignKey('AGENTS.AGENT_CODE', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    
    AGENT           = relationship('AGENT')


class ORDER(Base):
    __tablename__ = 'ORDERS'

    ORD_NUM         = Column(String, primary_key=True)
    ORD_AMOUNT      = Column(CHAR(12), nullable=False)
    ADVANCE_AMOUNT  = Column(CHAR(12), nullable=False)
    ORD_DATE        = Column(Date, nullable=False)
    CUST_CODE       = Column(ForeignKey('CUSTOMER.CUST_CODE', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    AGENT_CODE      = Column(ForeignKey('AGENTS.AGENT_CODE', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    ORD_DESCRIPTION = Column(String(60), nullable=False)
    
    AGENT           = relationship('AGENT')
    CUSTOMER        = relationship('CUSTOMER')
