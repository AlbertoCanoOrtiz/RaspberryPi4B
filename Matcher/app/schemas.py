from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, BLOB, Numeric 
from sqlalchemy.orm import relationship
from database import Base

class Animal(Base):
  __tablename__ = 'animal'
  size = Column(Integer, primary_key = True)
  body = Column(Integer)
  chest = Column(Integer)
  neck = Column(Integer)
  breed = Column(Integer)
  color = Column(varchar(100))
  firstImage = Column(BLOB)
  secondImage = Column(BLOB)
  thirdImage = Column(BLOB)
  fourthImage = Column(BLOB)
  fifthImage = Column(BLOB)
  sixthImage = Column(BLOB)
  seventhImage = Column(BLOB)
  eighthImage = Column(BLOB)
  ninthImage = Column(BLOB)
  tenthImage = Column(BLOB)
  signDate = Column(DateTime)
  statusInd = Column(Boolean, default = True)

class Sociopath(Base):
  __tablename__ = 'sociopath'
  rfc =	Column(String(100),primary_key = True)
  gender = Column(String(10))
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  firtsimage = Column(BLOB)
  secondImage = Column(BLOB)
  thirdImage = Column(BLOB)
  signDate = Column(DateTime)
  statusInd = Column(Boolean. default = True) 

class Adopter(Base):
  __tablename__ = 'adopter'
  rfc =	Column(String(100), primary_key = True)
  gender =
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  email = Column(String(100))
  telephone = Column(Numeric(10))
  celphone = Column(Numeric(10))
  firtsimage =	Column(BLOB)
  secondImage =	Column(BLOB)
  thirdImage = Column(BLOB)
  signDate = Column(DateTime)
  statusInd = Column(Boolean, default = True)

class Partnership(Base):
  __tablename__ = 'partnership'
  rfc =	Column(String(100), primary_key = True)
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  email = Column(String(100))
  telephone = Column(Numeric(10))
  celphone = Column(Numeric(10))
  url = Column(String(100))
  firtsimage = Column(BLOB)
  secondImage = Column(BLOB)
  thirdImage = Column(BLOB)
  signDate = Column(DateTime)
  statusInd = Column(Boolean, default = True)
