from sqlalchemy.orm import Session
import models, schemas
import json

def get_adopter_( db: Session, skip: int = 0, limit: int = 1000 ):
  db_adopter = db.query(schemas.Adopter).offset(skip).limit(limit).all()
  return db_adopter

def get_animal_( db: Session, skip: int  = 0, limit: int = 1000 ):
  db_animal = db.query(schemas.Animal).offset(skip).limit(limit).all()
  db_animal = [it.__dict__ for it in db_animal].pop()
  del db_animal['_sa_instance_state']
  return db_animal

def get_partnership_(db: Session, skip: int=  0, limit: int = 1000 ):
  db_partnership = db.query(schemas.Partnership).offset(skip).limit(limit).all()
  db_partnership = [it.__dict__ for it in db_partnership].pop()
  del db_partnership['_sa_instance_state']
  return db_partnership
  
def get_sociopath_( db: Session, skip: int = 0, limit: int= 1000 ):
  db_sociopath = db.query(schemas.Sociophat).offset(skip).limit(limit).all()
  db_sociopath = [it.__dict__ for it in db_sociopath].pop()
  del db_sociopath['_sa_instance_state']
  return db_sociopath
