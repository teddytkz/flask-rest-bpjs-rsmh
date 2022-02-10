from app import app
from flask import Flask,request,jsonify

from app.controller import BpjsController
from app.controller import DataController

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