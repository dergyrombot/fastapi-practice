from typing import List
from pydantic import BaseModel

# Buku inside UserDisplay
class Buku(BaseModel):
  nama: str
  penulis: str
  penerbit: str
  genre: str
  class Config():
    orm_mode = True

class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Buku] = []
  class Config():
    orm_mode = True

# User inside BukuDisplay
class User(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True

class BukuBase(BaseModel):
  nama: str
  penulis: str
  penerbit: str
  genre: str
  

class BukuDisplay(BaseModel):
  nama: str
  penulis: str
  penerbit: str
  genre: str
  class Config():
    orm_mode = True

