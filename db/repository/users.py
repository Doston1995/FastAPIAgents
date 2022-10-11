from sqlalchemy.orm import Session
from db.models import User
from schemas.users import UserCreate, UserShow, UserUpdate, UserDelete
import datetime, uuid
from db.hashing import Hasher

def list_users(db : Session):
    users = db.query(User).all()
    return users


def create_user(user: UserCreate, db: Session):
    user_date = str(datetime.datetime.now())
    user_id   = str(uuid.uuid1())
    user_object = User(
        id = user_id,
        username   = user.username,
        password   = Hasher.get_password_hash(user.password),
        email      = user.email,
        first_name = user.first_name,
        last_name  = user.last_name,
        gender     = user.gender,
        create_at  = user_date,
        status     = "1"
    )
    db.add(user_object)
    db.commit()
    db.refresh(user_object)
    return user_object


def retreive_user(user_id:str, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    return user


def update_user(user_id:str, user: UserShow, db: Session):
    existing_user = db.query(User).filter(User.id == user_id)
    if not existing_user.first():
        return 0
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_user(user_id:str, db: Session):
    existing_user = db.query(User).filter(User.id == user_id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1