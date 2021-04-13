from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./fastapi.db'
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        #     "encoding": "utf8",
        "check_same_thread": False
    })

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()