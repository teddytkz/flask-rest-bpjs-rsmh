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
from app.model.bpjs_rencana_ri_response import rencanaRiResponse
from app.model.bpjs_rencana_kontrol_response import rencanaKontrolResponse


app = Flask(__name__)
cors = CORS(app)

config = dotenv_values(".env")
host = config['BPJS_HOST']
consid = config['BPJS_CONST_ID']
secret = config['BPJS_SECRET_KEY']
user_key = config['BPJS_USER_KEY']
is_encrypt = config['IS_ENCRYPT']

def save_sep_req(data,status):
    data_request = data['request']['t_sep']
    data_sep_req = sepRequest(
        status_created_sep = status,
        noKartu = data_request['noKartu'],
        tglSep = data_request['tglSep'],
        ppkPelayanan = data_request['ppkPelayanan'],
        jnsPelayanan = data_request['jnsPelayanan'],
        klsRawat_klsRawatHak = data_request['klsRawat']['klsRawatHak'],
        klsRawat_klsRawatNaik = data_request['klsRawat']['klsRawatNaik'],
        klsRawat_pembiayaan = data_request['klsRawat']['pembiayaan'],
        klsRawat_penanggung_jawab = data_request['klsRawat']['penanggungJawab'],
        noMR = data_request['noMR'],
        rujukan_asalRujukan = data_request['rujukan']['asalRujukan'],
        rujukan_tglRujukan = data_request['rujukan']['tglRujukan'],
        rujukan_noRujukan = data_request['rujukan']['noRujukan'],
        rujukan_ppkRujukan = data_request['rujukan']['ppkRujukan'],
        catatan = data_request['catatan'],
        diagAwal = data_request['diagAwal'],
        poli_tujuan = data_request['poli']['tujuan'],
        poli_eksekutif = data_request['poli']['eksekutif'],
        cob = data_request['cob']['cob'],
        katarak_katarak = data_request['katarak']['katarak'],
        jaminan_lakaLantas = data_request['jaminan']['lakaLantas'],
        jaminan_noLP = data_request['jaminan']['noLP'],
        jaminan_penjamin_tglKejadian = data_request['jaminan']['penjamin']['tglKejadian'],
        jaminan_penjamin_keterangan = data_request['jaminan']['penjamin']['keterangan'],
        jaminan_penjamin_suplesi_suplesi = data_request['jaminan']['penjamin']['suplesi']['suplesi'],
        jaminan_penjamin_suplesi_noSepSuplesi = data_request['jaminan']['penjamin']['suplesi']['noSepSuplesi'],
        jaminan_penjamin_suplesi_lokasiLaka_kdPropinsi = data_request['jaminan']['penjamin']['suplesi']['lokasiLaka']['kdPropinsi'],
        jaminan_penjamin_suplesi_lokasiLaka_kdKabupaten = data_request['jaminan']['penjamin']['suplesi']['lokasiLaka']['kdKabupaten'],
        jaminan_penjamin_suplesi_lokasiLaka_kdKecamatan = data_request['jaminan']['penjamin']['suplesi']['lokasiLaka']['kdKecamatan'],
        tujuanKunj = data_request['tujuanKunj'],
        flagProcedure = data_request['flagProcedure'],
        kdPenunjang = data_request['kdPenunjang'],
        assesmentPel = data_request['assesmentPel'],
        skdp_noSurat = data_request['skdp']['noSurat'],
        skdp_kodeDPJP = data_request['skdp']['kodeDPJP'],
        dpjpLayan = data_request['dpjpLayan'],
        noTelp = data_request['noTelp'],
        user = data_request['user'],
    )
    db.session.add(data_sep_req)
    db.session.commit()
    return 'Success Save To DB'

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

def save_spri_res(data):
    response = data['response']
    data_spri_res = rencanaRiResponse(
        noSPRI = response['noSPRI'],
        tglRencanaKontrol = response['tglRencanaKontrol'],
        namaDokter = response['namaDokter'],
        noKartu = response['noKartu'],
        nama = response['nama'],
        kelamin = response['kelamin'],
        tlgLahir = response['tglLahir'],
        namaDiagnosa = response['namaDiagnosa'],
    )
    db.session.add(data_spri_res)
    db.session.commit()
    save_data_spri = {
            "status" : data['metaData']['code'],
            "message" : data['metaData']['message'],
            "nosep" : data['response']['noSPRI'],
            # "datax" : data
        }
    return save_data_spri

def save_rencana_kontrol_res(data):
    response = data['response']
    data_rencana_kontrol_res = rencanaKontrolResponse(
        noSuratKontrol = response['noSuratKontrol'],
        tglRencanaKontrol = response['tglRencanaKontrol'],
        namaDokter = response['namaDokter'],
        noKartu = response['noKartu'],
        nama = response['nama'],
        kelamin = response['kelamin'],
        tlgLahir = response['tglLahir']
    )
    db.session.add(data_rencana_kontrol_res)
    db.session.commit()
    save_data_rencana_kontrol = {
            "status" : data['metaData']['code'],
            "message" : data['metaData']['message'],
            "nosep" : data['response']['noSuratKontrol'],
            # "datax" : data
        }
    return save_data_rencana_kontrol
