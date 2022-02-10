from app import app
from flask import Flask,request,jsonify

from app.controller import BpjsController
from app.controller import DataController

@app.route('/api/referensi/faskes',methods=['GET'])
def referensi_faskes():
    # data = request.get_json()
    end_point='referensi/faskes/'+request.args.get('faskes')+'/'+request.args.get('jenis_faskes')
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)
    

@app.route('/api/referensi/diagnosa',methods=['GET'])
def referensi_diagnosa():
    nama_diagnosa = request.args.get('nama_diagnosa')
    end_point='referensi/diagnosa/'+nama_diagnosa
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/referensi/poli',methods=['GET'])
def referensi_poli():
    nama_poli = request.args.get('nama_poli')
    end_point='referensi/poli/'+nama_poli
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/referensi/dokter_dpjp',methods=['GET'])
def referensi_dokter_dpjp():
    jenis_pelayanan = request.args.get('jenis_pelayanan')
    kode_spesialis = request.args.get('kode_poli')
    tanggal_sep = str(request.args.get('tanggal_sep'))
    end_point="referensi/dokter/pelayanan/"+jenis_pelayanan+"/tglPelayanan/"+tanggal_sep+"/Spesialis/"+kode_spesialis
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)