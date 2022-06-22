# generated by fastapi-codegen:
#   filename:  finder.yaml
#   timestamp: 2022-02-24T21:51:03+00:00

#from __future__ import annotations

from typing import Union

from fastapi import Depends, FastAPI, HTTPException

from models import Adopter, Animal, Error, Partnership, Sociopath

from database import SessionLocal, engine

import schemas, crud

from sqlalchemy.orm import Session

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(version='1.0', title='Matcher', servers=[{'url': 'localhost:3000'}], )

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.get('/adopter', response_model=Adopter, responses={'default': {'model': Error}})
def get_adopter( skip: int = 0, limit: int= 1000, db: Session = Depends(get_db) ) -> Union[Adopter, Error]:
  adopter = crud.get_adopter_(skip=skip, limit=limit, db = db)
  return adopter


@app.get('/animal', response_model=Animal, responses={'default': {'model': Error}})
def get_animal( skip: int = 0, limit: int= 1000, db: Session = Depends(get_db) ) -> Union[Animal, Error]:
  animal = crud.get_animal_(skip = skip, limit = limit, db = db)
  return animal


@app.get(
    '/partnership', response_model=Partnership, responses={'default': {'model': Error}}
)
def get_partnership( skip: int = 0, limit: int= 1000, db: Session = Depends(get_db) ) -> Union[Partnership, Error]:
  partnership = crud.get_partnership_(skip = skip, limit = limit, db = db)
  return partnership


@app.get(
    '/sociopath', response_model=Sociopath, responses={'default': {'model': Error}}
)
def get_sociopath( skip: int = 0, limit: int= 1000, db: Session = Depends(get_db) ) -> Union[Sociopath, Error]:
  sociopath = crud.get_sociopath_(skip = skip, limit = limit, db = db)
  return sociopath
