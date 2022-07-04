from fastapi import FastAPI
import uvicorn
from sqlmodel import create_engine, SQLModel

import repos.gem_repository
from models.gem_models import *

app = FastAPI(debug=True)

# engine = create_engine('postgresql://postgres:postgrespw@localhost:55000/postgres', echo=True)
conn_str = "postgresql://postgres:postgrespw@localhost:55000/postgres"
engine = create_engine(conn_str, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.get('/gems')
def gems():
    gems = repos.gem_repository.select_all_gems()
    return {'gems': gems}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
    create_db_and_tables()
