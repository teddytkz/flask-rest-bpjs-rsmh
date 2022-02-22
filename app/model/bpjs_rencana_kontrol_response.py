from app import db
from datetime import datetime

class rencanaKontrolResponse(db.Model):
    id = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    noSuratKontrol = db.Column(db.String(250),nullable=True)
    tglRencanaKontrol = db.Column(db.String(250),nullable=True)
    namaDokter = db.Column(db.String(250),nullable=True)
    noKartu = db.Column(db.String(250),nullable=True)
    nama = db.Column(db.String(250),nullable=True)
    kelamin = db.Column(db.String(250),nullable=True)
    tlgLahir = db.Column(db.String(250),nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr_(self):
        return '<rencanaKontrolResponse {}>'.format(self.name)