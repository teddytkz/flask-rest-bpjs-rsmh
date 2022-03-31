from app import app
from flask import Flask,request,jsonify

from app.controller import BpjsController
from app.controller import DataController

@app.route('/api/rencanakontrol/insert',methods=['POST'])
def rencanakontrol_insert():
    data = request.get_json()
    end_point = 'RencanaKontrol/insert'
    method = 'post'
    payload = data
    send_rencana_kontrol = BpjsController.bridging_data(end_point,method,payload)
    if(send_rencana_kontrol['metaData']['code']=='200'):
        save_spri_res = DataController.save_rencana_kontrol_res(send_rencana_kontrol)
        res_data_spri = {
            "metadata":{
                "status" : send_rencana_kontrol['metaData']['code'],
                "message" : send_rencana_kontrol['metaData']['message'],
            },
            "data":{
                "nomor_spri" : send_rencana_kontrol['response']['noSuratKontrol']
            }
        }
    else:
        res_data_spri = {
            "metadata":{
                "status" : send_spri['metaData']['code'],
                "message" : send_spri['metaData']['message'],
            }
    }
    return res_data_spri

@app.route('/api/rencanakontrol/insertspri',methods=['POST'])
def rencanakontrol_insert_spri():
    data = request.get_json()
    end_point = 'RencanaKontrol/insertSPRI'
    method = 'post'
    payload = data
    send_spri = BpjsController.bridging_data(end_point,method,payload)
    if(send_spri['metaData']['code']=='200'):
        save_spri_res = DataController.save_spri_res(send_spri)
        res_data_spri = {
            "metadata":{
                "status" : send_spri['metaData']['code'],
                "message" : send_spri['metaData']['message'],
            },
            "data":{
                "nomor_spri" : send_spri['response']['noSPRI']
            }
        }
    else:
        res_data_spri = {
            "metadata":{
                "status" : send_spri['metaData']['code'],
                "message" : send_spri['metaData']['message'],
            }
    }
    return res_data_spri
    # return BpjsController.bridging(end_point,method,payload)

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

@app.route('/api/rencanakontrol/listspesialistik')
def rencanakontrol_list_spesialistik():
    jenis_kontrol = request.args.get('jenis_kontrol')
    nomor = request.args.get('nomor')
    tanggal_rencana_kontrol = request.args.get('tanggal_rencana_kontrol')
    method = 'get'
    payload = ''
    end_point = 'RencanaKontrol/ListSpesialistik/JnsKontrol/'+jenis_kontrol+'/nomor/'+nomor+'/TglRencanaKontrol/'+tanggal_rencana_kontrol
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/rencanakontrol/listdokterspesialistik')
def rencanakontrol_list_dokter_spesialistik():
    jenis_kontrol = request.args.get('jenis_kontrol')
    kode_poli = request.args.get('kode_poli')
    tanggal_rencana_kontrol = request.args.get('tanggal_rencana_kontrol')
    method = 'get'
    payload = ''
    end_point = 'RencanaKontrol/JadwalPraktekDokter/JnsKontrol/'+jenis_kontrol+'/KdPoli/'+kode_poli+'/TglRencanaKontrol/'+tanggal_rencana_kontrol
    return BpjsController.bridging(end_point,method,payload)

# @app.route('/api/rencanakontrol/update')
# def rencanakontrol_update():
#     no_surat_kontrol = request.args.get('no_surat_kontrol')
#     no_sep = request.args.get('no_sep')
#     kode_dokter = request.args.get('kode_dokter')
#     poli_kontrol = request.args.get('poli_kontrol')
#     tgl_rencana_kontrol = request.args.get('tgl_rencana_kontrol')

@app.route('/api/rencanakontrol/delete')
def rencanakontrol_delete():
    no_surat_kontrol = request.args.get('no_surat_kontrol')
    method = 'delete'
    payload = {
        "request":{
            "t_suratkontrol":{
                "noSuratKontrol": no_surat_kontrol,
                "user": "Teddy"
            }
        }
    }
    end_point = 'RencanaKontrol/Delete'
    return BpjsController.bridging(end_point,method,payload)

