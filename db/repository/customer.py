from sqlalchemy.orm import Session
from db.models import CUSTOMER
from schemas.customer import CustomerCreate, CustomerShow
import datetime, uuid

def list_customers(db : Session):
    customers = db.query(CUSTOMER).all()
    return customers


def create_customer(customer: CustomerCreate, db: Session):
    create_at = str(datetime.datetime.now())
    customer_object = CUSTOMER(
                                CUST_CODE = customer.CUST_CODE,
                                CUST_NAME = customer.CUST_NAME,
                                CUST_CITY = customer.CUST_CITY,
                                WORKING_AREA = customer.WORKING_AREA,
                                CUST_COUNTRY = customer.CUST_COUNTRY,
                                GRADE = customer.GRADE,
                                OPENING_AMT = customer.OPENING_AMT,
                                RECEIVE_AMT = customer.RECEIVE_AMT,
                                PAYMENT_AMT = customer.PAYMENT_AMT,
                                OUTSTANDING_AMT = customer.OUTSTANDING_AMT,
                                PHONE_NO = customer.PHONE_NO,
                                CREATE_AT = create_at,
                                AGENT_CODE = customer.AGENT_CODE
    )
    db.add(customer_object)
    db.commit()
    db.refresh(customer_object)
    return customer_object
    

def retreive_customer(cust_code:str, db:Session):
    customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code).first()
    return customer


def update_customer(cust_code:str, customer: CustomerShow, db: Session):
    existing_customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code)
    if not existing_customer.first():
        return 0
    existing_customer.update(customer.__dict__)
    db.commit()
    return 1


def delete_customer(cust_code:str, db: Session):
    existing_customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code)
    if not existing_customer.first():
        return 0
    existing_customer.delete(synchronize_session=False)
    db.commit()
    return 1