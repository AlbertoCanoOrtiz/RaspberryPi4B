# generated by fastapi-codegen:
#   filename:  finder.yaml
#   timestamp: 2022-02-24T21:51:03+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint, constr


class Error(BaseModel):
    code: int
    message: str


class Animal(BaseModel):
    size: conint(ge=0, le=100)
    body: Optional[conint(ge=0, le=100)] = None
    chest: Optional[conint(ge=0, le=100)] = None
    neck: Optional[conint(ge=0, le=100)] = None
    breed: constr(regex=r'\w', min_length=10)
    signDate: Optional[datetime] = None
    statusInd: Optional[bool] = None


class Sociopath(BaseModel):
    rfc: Optional[constr(regex=r'[a-zA-Z0-9]+', min_length=13)] = None
    street: constr(regex=r'\w', min_length=1, max_length=100)
    number: int
    secction: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    district: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    village: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    country: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    code: Optional[int] = None
    signDate: Optional[datetime] = None


class Adopter(BaseModel):
    rfc: constr(regex=r'[a-zA-Z0-9]+', min_length=13)
    street: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    number: Optional[int] = None
    secction: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    district: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    village: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    country: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    code: Optional[int] = None
    signDate: Optional[datetime] = None


class Partnership(BaseModel):
    rfc: constr(regex=r'[a-zA-Z0-9]+', min_length=13)
    street: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    number: Optional[int] = None
    secction: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    district: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    village: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    country: Optional[constr(regex=r'\w', min_length=1, max_length=100)] = None
    code: Optional[int] = None
    signDate: Optional[datetime] = None
