import databases
from db.session import SQLALCHEMY_DATABASE_URL

async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__('postgresql'):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
    except Exception as e:
        print("Looks like there is some problem in connection,see below traceback")
        raise e
    


async def check_db_disconnected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("postgresql"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if database.is_connected:
                await database.disconnect()
    except Exception as e:
        raise e