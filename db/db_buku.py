from sqlalchemy.orm.session import Session
from db.models import DbBuku
from schemas import BukuBase


def create_buku(db: Session, request: BukuBase):
  new_buku = DbBuku(
    nama = request.nama,
    penulis = request.penulis,
    penerbit= request.penerbit,
    genre = request.genre
  )
  db.add(new_buku)
  db.commit()
  db.refresh(new_buku)
  return new_buku

def get_buku(db: Session, id: int):
  buku = db.query(DbBuku).filter(DbBuku.id == id).first()
  # Handle errors
  return buku

def get_all_buku(db: Session):
  return db.query(DbBuku).all()