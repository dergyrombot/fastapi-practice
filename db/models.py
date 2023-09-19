from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbBuku', back_populates='user')

class DbBuku(Base):
  __tablename__= 'buku'
  id = Column(Integer, primary_key=True, index=True)
  nama = Column(String)
  penulis = Column(String)
  penerbit = Column(String)
  genre = Column(String)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("DbUser", back_populates='items')


