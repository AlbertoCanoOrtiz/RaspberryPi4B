# generated by fastapi-codegen:
#   filename:  matcher.yaml
#   timestamp: 2022-07-20T17:55:29+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, conint, constr


class Success(BaseModel):
    code: int
    message: str


class Error(BaseModel):
    code: int
    message: str


class Color(Enum):
    black = 'black'
    white = 'white'
    red = 'red'
    green = 'green'
    blue = 'blue'


class Animal(BaseModel):
    size: conint(ge=0, le=100)
    body: Optional[conint(ge=0, le=100)] = None
    chest: Optional[conint(ge=0, le=100)] = None
    neck: Optional[conint(ge=0, le=100)] = None
    breed: constr(regex=r'^\w', min_length=10)
    color: Color
    firstImage: Optional[bytes] = None
    secondImage: Optional[bytes] = None
    thirdImage: Optional[bytes] = None
    fourthImage: Optional[bytes] = None
    fifthImage: Optional[bytes] = None
    sixthImage: Optional[bytes] = None
    seventhImage: Optional[bytes] = None
    eighthImage: Optional[bytes] = None
    ninthImage: Optional[bytes] = None
    tenthImage: Optional[bytes] = None
    signDate: Optional[str] = None
    statusInd: Optional[bool] = None


class Sociopath(BaseModel):
    rfc: Optional[constr(regex=r'[a-zA-Z0-9]+', min_length=13)] = None
    gender: constr(min_length=8, max_length=9)
    street: constr(regex=r'\w', min_length=1, max_length=100)
    number: int
    section: constr(regex=r'\w', min_length=1, max_length=100)
    district: constr(regex=r'\w', min_length=1, max_length=100)
    village: constr(regex=r'\w', min_length=1, max_length=100)
    country: constr(regex=r'\w', min_length=1, max_length=100)
    code: Optional[int] = None
    firstImage: Optional[bytes] = None
    secondImage: Optional[bytes] = None
    thirdImage: Optional[bytes] = None
    signDate: Optional[datetime] = None
    statusInd: Optional[bool] = None


class Adopter(BaseModel):
    rfc: constr(regex=r'[a-zA-Z0-9]+', min_length=13)
    gender: Optional[constr(min_length=8, max_length=9)] = None
    street: constr(regex=r'\w', min_length=1, max_length=100)
    number: int
    section: constr(regex=r'\w', min_length=1, max_length=100)
    district: constr(regex=r'\w', min_length=1, max_length=100)
    village: constr(regex=r'\w', min_length=1, max_length=100)
    country: constr(regex=r'\w', min_length=1, max_length=100)
    code: Optional[int] = None
    email: Optional[EmailStr] = None
    telephone: Optional[conint(ge=10, le=10)] = None
    celphone: Optional[conint(ge=10, le=10)] = None
    firstImage: Optional[bytes] = None
    secondImage: Optional[bytes] = None
    thirdImage: Optional[bytes] = None
    signDate: Optional[datetime] = None
    statusInd: Optional[bool] = None


class Partnership(BaseModel):
    rfc: constr(regex=r'[a-zA-Z0-9]+', min_length=13)
    street: constr(regex=r'\w', min_length=1, max_length=100)
    number: int
    section: constr(regex=r'\w', min_length=1, max_length=100)
    district: constr(regex=r'\w', min_length=1, max_length=100)
    village: constr(regex=r'\w', min_length=1, max_length=100)
    country: constr(regex=r'\w', min_length=1, max_length=100)
    code: Optional[int] = None
    email: Optional[EmailStr] = None
    telephone: Optional[conint(ge=1000000000, le=9999999999)] = None
    celphone: Optional[conint(ge=1000000000, le=9999999999)] = None
    url: Optional[
        constr(
            regex=r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)\Z'
        )
    ] = None
    firstImage: Optional[bytes] = None
    secondImage: Optional[bytes] = None
    thirdImage: Optional[bytes] = None
    signDate: Optional[datetime] = None
    statusInd: Optional[bool] = None
