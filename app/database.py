from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
import os

engine = create_engine(os.environ['DATABASE_URL'], echo=True)

class Base(DeclarativeBase):
    pass

def get_db():
    with Session(engine) as db:
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
