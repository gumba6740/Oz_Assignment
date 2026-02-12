from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


def make_engine(db_info):
    url = URL.create(
        drivername=db_info["driver"],
        username=db_info["user"],
        password=db_info["password"],
        host=db_info["host"],
        port=db_info["port"],
        database=db_info["database"],
        query={"charset": db_info["charset"]}    
    )
    
    return create_engine(url)

def make_session(engine):
    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )