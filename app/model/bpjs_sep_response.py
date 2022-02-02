from app import db
from datetime import datetime

class sepResponse(db.Model):
    id = db.Column(db.BigInteger,primary_key = True,autoincrement = True)
    catatan = db.Column(db.String(250),nullable = True)
    diagnosa = db.Column(db.String(250),nullable = True)
    jnspelayanan = db.Column(db.String(250),nullable = True)
    kelasrawat = db.Column(db.String(250),nullable = True)
    nosep = db.Column(db.String(250),nullable = True)
    penjamin = db.Column(db.String(250),nullable = True)
    peserta_asuransi = db.Column(db.String(250),nullable = True)
    peserta_hakkelas = db.Column(db.String(250),nullable = True)
    peserta_jnspeserta = db.Column(db.String(250),nullable = True)
    peserta_kelmain = db.Column(db.String(250),nullable = True)
    peserta_nama = db.Column(db.String(250),nullable = True)
    peserta_nomorkartu = db.Column(db.String(250),nullable = True)
    peserta_nomr = db.Column(db.String(250),nullable = True)
    peserta_tgllahir = db.Column(db.DateTime,nullable = True)
    informasi_dinsos = db.Column(db.String(250),nullable = True)
    informasi_prolanisprb = db.Column(db.String(250),nullable = True)
    informasi_nosktm = db.Column(db.String(250),nullable = True)
    poli = db.Column(db.String(250),nullable = True)
    polieksekutif = db.Column(db.String(250),nullable = True)
    tglsep = db.Column(db.DateTime,nullable = True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr_(self):
        return '<sepResponse {}>'.format(self.name)