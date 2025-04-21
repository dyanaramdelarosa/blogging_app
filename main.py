import os
import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select

from models.models import User, BlogPost


def setup_db_engine():
    load_dotenv()
    db_username = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    postgresql_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(postgresql_url)

    return create_engine(postgresql_url, echo=True)


app = FastAPI()
engine = setup_db_engine()
SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/version")
def app_version():
    return {"version": "1.0.0"}


@app.post("/register")
def register(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)