from app import app,db
from flask import Flask,request,jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from datetime import datetime
import json

from app.controller import BpjsController
from app.controller import DataController

cors = CORS(app)
config = dotenv_values(".env")
kodeppk = config['BPJS_KODE_PPK']

from app.router import rencanaKontrol_router
from app.router import sep_router

#Nomor Rujukan = 080209020122P000007
#Nomor Kartu = 0002084341004

# nama = request.get_json() ==> Using Json
# str(datetime.today().strftime('%Y-%m-%d'))
# request.args.get('nm')
# request.form['nm]



@app.route('/api/test',methods=['GET'])
def test():
    data = request.get_json()
    a = BpjsController.test()
    b = str(datetime.today().strftime('%Y-%m-%d'))
    return a+" "+b
    
## Peserta

@app.route('/api/peserta/nik',methods=['POST'])
def referensi_peserta_nik():
    end_point = 'Peserta/nik/'+request.form['nokartu']+'/tglSEP/'+str(datetime.today().strftime('%Y-%m-%d'))
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/peserta/nokartu',methods=['POST'])
def referensi_peserta_nokartu():
    end_point = 'Peserta/nokartu/'+request.form['nokartu']+'/tglSEP/'+str(datetime.today().strftime('%Y-%m-%d'))
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

    

## Referensi

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


#### Rujukan ###
@app.route('/api/rujukan',methods=['GET'])
def referensi_cari_rujukan():
    nomor_rujukan = request.args.get('nomor_rujukan')
    end_point = 'Rujukan/'+nomor_rujukan
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rujukan/rs',methods=['GET'])
def referensi_cari_rujukan_rs():
    nomor_rujukan = request.args.get('nomor_rujukan')
    end_point = 'Rujukan/RS/'+nomor_rujukan
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rujukan/peserta/<param>',methods=['GET'])
def referensi_cari_rujukan_peserta(param):
    end_point='Rujukan/Peserta/'+param
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rujukan/<param>',methods=['GET'])
def referensi_cari_rujukan_no_rujukan(param):
    end_point='Rujukan/'+param
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rujukan/list/peserta',methods=['POST'])
def referensi_cari_list_rujukan_no_rujukan():
    nomor_kartu=request.form['nomor_kartu']
    end_point='Rujukan/List/Peserta/'+nomor_kartu
    method = 'get'
    payload = ''
    dataParser = BpjsController.bridging_data(end_point,method,payload)
    datas={}
    if(dataParser['metaData']['code']!="200"):
        datas['data']=[]
    else:
        datas['data']=[]
        for x in dataParser['response']['rujukan']:
            no = 0
            data = {
                    "no":no+1,
                    "no_rujukan":"<a href='#' class='label bg-blue' id='btn-noKunjungan' no_kunjungan='"+x['noKunjungan']+"'>"+x['noKunjungan']+"</a>",
                    "tanggal_rujukan":x['tglKunjungan'],
                    "no_kartu":x['peserta']['noKartu'],
                    "nama":x['peserta']['nama'],
                    "ppk_perujuk":x['provPerujuk']['nama'],
                    "spesialis":x['poliRujukan']['kode'] + "( "+x['poliRujukan']['nama']+" )"
                }
            datas['data'].append(data) 
    return datas

@app.route('/api/rujukan/rs/list/peserta',methods=['POST'])
def referensi_cari_list_rujukan_rs_no_rujukan():
    nomor_kartu=request.form['nomor_kartu']
    end_point='Rujukan/RS/List/Peserta/'+nomor_kartu
    method = 'get'
    payload = ''
    dataParser = BpjsController.bridging_data(end_point,method,payload)
    datas={}
    datas['data']=[]
    for x in dataParser['rujukan']:
        no = 0
        data = {
                "no":no+1,
                "no_rujukan":"<span class='badge badge-primary'><a href='#' id='btn-noKunjungan' no_kunjungan='"+x['noKunjungan']+"'>"+x['noKunjungan']+"</a></span>",
                "tanggal_rujukan":x['tglKunjungan'],
                "no_kartu":x['peserta']['noKartu'],
                "nama":x['peserta']['nama'],
                "ppk_perujuk":x['provPerujuk']['nama'],
                "spesialis":x['poliRujukan']['kode'] + "( "+x['poliRujukan']['nama']+" )"
            }
        datas['data'].append(data)
    return datas






