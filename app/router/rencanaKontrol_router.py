from app import app
from flask import Flask,request,jsonify

from app.controller import BpjsController
from app.controller import DataController

@app.route('/api/rencanakontrol/cari/sep',methods=['GET'])
def rencanakontrol_cari_sep():
    no_sep = request.args.get('no_sep')
    end_point = 'RencanaKontrol/nosep/'+no_sep
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rencanakontrol/cari/suratkontrol')
def rencanakontrol_cari_suratkontrol():
    no_surat_kontrol = request.args.get('nosuratkontrol')
    end_point = 'RencanaKontrol/noSuratKontrol/'+no_surat_kontrol
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rencanakontrol/cari/suratkontrol/nokartu')
def rencanakontrol_cari_suratkontrol_nokartu():
    bulan = request.args.get('bulan')
    tahun = request.args.get('tahun')
    nokartu = request.args.get('nokartu')
    filter_format = request.args.get('filter') #1. Tanggal Entry 2. Tanggal Rencana Kontrol
    end_point = 'RencanaKontrol/ListRencanaKontrol/Bulan'+bulan+'/Tahun/'+tahun+'/nokartu/'+nokartu+'/filter/'+filter_format
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)