from app import app,db
from flask import Flask, request, jsonify
from dotenv import dotenv_values
from Crypto.Cipher import AES
from datetime import datetime
import lzstring
import requests
import hashlib
import base64
import hmac
import json
import os
from flask_cors import CORS

from app.model.bpjs_sep_request import sepRequest
from app.model.bpjs_sep_response import sepResponse


app = Flask(__name__)
cors = CORS(app)

config = dotenv_values(".env")
host = config['BPJS_HOST']
consid = config['BPJS_CONST_ID']
secret = config['BPJS_SECRET_KEY']
user_key = config['BPJS_USER_KEY']
is_encrypt = config['IS_ENCRYPT']

def save_sep_req(data):
    request = data['request']['t_sep']
    data_sep_req = sepRequest(
        noKartu = data['noKartu'],
        tglSep = data['noKartu'],
        ppkPelayanan = data['noKartu'],
        # klsRawat_klsRawatHak = 
        # klsRawat_klsRawatNaik = 
        # klsRawat_pembiayaan = 
        # klsRawat_penanggung_jawab = 
        # noMR =
        # rujukan_asalRujukan = 
        # rujukan_tglRujukan = 
        # rujukan_noRujukan = 
        # rujukan_ppkRujukan = 
        # catatan = 
        # diagAwal = 
        # poli_tujuan = 
        # poli_eksekutif = 
        # cob = 
        # katarak_katarak = 
        # jaminan_lakaLantas = 
        # jaminan_penjamin_tglKejadian = 
        # jaminan_penjamin_keterangan = 
        # jaminan_penjamin_suplesi_suplesi = 
        # jaminan_penjamin_suplesi_noSepSuplesi = 
        # jaminan_penjamin_suplesi_lokasiLaka_kdPropinsi = 
        # jaminan_penjamin_suplesi_lokasiLaka_kdKabupaten = 
        # jaminan_penjamin_suplesi_lokasiLaka_kdKecamatan = 
        # tujuanKunj = 
        # flagProcedure = 
        # kdPenunjang = 
        # assesmentPel = 
        # skdp_noSurat = 
        # skdp_kodeDPJP = 
        # dpjpLayan = 
        # noTelp = 
        # user = 
        # created_at = 
        # updated_at = 
    )
    db.session.add(data_sep_req)
    db.session.commit()
    return 'Save To DB'

def save_sep_res(data):
    response = data['response']['sep']
    data_sep_res = sepResponse(
        catatan = response['catatan'],
        diagnosa = response['diagnosa'],
        jnspelayanan = response['jnsPelayanan'],
        kelasrawat = response['kelasRawat'],
        nosep = response['noSep'],
        penjamin = response['penjamin'],
        peserta_asuransi = response['peserta']['asuransi'],
        peserta_hakkelas = response['peserta']['hakKelas'],
        peserta_jnspeserta = response['peserta']['jnsPeserta'],
        peserta_kelmain = response['peserta']['kelamin'],
        peserta_nama = response['peserta']['nama'],
        peserta_nomorkartu = response['peserta']['noKartu'],
        peserta_nomr = response['peserta']['noMr'],
        peserta_tgllahir = response['peserta']['tglLahir'],
        informasi_dinsos = response['informasi']['dinsos'],
        informasi_prolanisprb = response['informasi']['prolanisPRB'],
        informasi_nosktm = response['informasi']['noSKTM'],
        poli = response['poli'],
        polieksekutif = response['poliEksekutif'],
        tglsep = response['tglSep'],
    )
    db.session.add(data_sep_res)
    db.session.commit()
    save_data_sep = {
            "status" : data['metaData']['code'],
            "message" : data['metaData']['message'],
            "nosep" : data['response']['sep']['noSep'],
            # "datax" : data
        }
    return save_data_sep
