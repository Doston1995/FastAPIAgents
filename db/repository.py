from sqlalchemy.orm import Session
from db.models import AGENT, CUSTOMER, ORDER
from db.schemas import AgentCreate, AgentShow, CustomerCreate, CustomerShow, OrderCreate, OrderShow


###################### Agents ###################
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


###################### Customers  ###################

def list_customers(db : Session):
    customers = db.query(CUSTOMER).all()
    return customers


def create_customer(customer: CustomerCreate, db: Session):
    customer_object = CUSTOMER(**customer.dict())
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


###################### Orders  ###################


def list_orders(db : Session):
    orders = db.query(ORDER).all()
    return orders


def create_order(order: OrderCreate, db: Session):
    order_object = ORDER(**order.dict())
    db.add(order_object)
    db.commit()
    db.refresh(order_object)
    return order_object
    

def retreive_order(ord_num:str, db:Session):
    order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num).first()
    return order


def update_order(ord_num:str, order: OrderShow, db: Session):
    existing_order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num)
    if not existing_order.first():
        return 0
    existing_order.update(order.__dict__)
    db.commit()
    return 1


def delete_order(ord_num:str, db: Session):
    existing_order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num)
    if not existing_order.first():
        return 0
    existing_order.delete(synchronize_session=False)
    db.commit()
    return 1