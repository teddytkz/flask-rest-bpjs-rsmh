from app import app
from flask import Flask,request,jsonify

from app.controller import BpjsController
from app.controller import DataController

@app.route('/api/sep/2.0/insert',methods=['POST'])
def sep_insert():
    end_point='SEP/2.0/insert'
    method = 'post'
    data = request.get_json()
    payload = data
    status = '0'
    send_sep = BpjsController.bridging_data(end_point,method,payload)
    if(send_sep['metaData']['code']=="200"):
        status = '1'
        save_data_sep = DataController.save_sep_res(send_sep)
        save_sep_req = DataController.save_sep_req(data,status)
        res_data_sep = {
            "metadata":{
                "status" : send_sep['metaData']['code'],
                "message" : send_sep['metaData']['message'],
            },
            "data":{
                "status_save" : save_sep_req,
                "nomor_sep" : send_sep['response']['sep']['noSep']
            }
        }
    elif(send_sep['metaData']['code']=="201"):
        save_sep_req = DataController.save_sep_req(data,status)
        res_data_sep = {
            "metadata":{
                "status" : send_sep['metaData']['code'],
                "message" : send_sep['metaData']['message'],
            },
            "data":{
                "status_save" : save_sep_req
            }
        }
    return res_data_sep

@app.route('/api/sep',methods=['GET'])
def sep_search():
    data = request.get_json()
    end_point='SEP/'+data['nomor_sep']
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/sep/2.0/delete',methods=['POST'])
def sep_2_delete():
    # data = request.get_json()
    nomor_sep = request.form['no_sep']
    user = request.form['user']
    end_point='SEP/2.0/delete'
    method = 'delete'
    payload = {
        "request": {
            "t_sep": {
                "noSep": nomor_sep,
                "user": user
            }
        }
    }
    return BpjsController.bridging(end_point,method,payload)

# @app.route('/api/sep/2.0/updatetanggalpulang')
# def update_tanggal_pulang():
#     data = request.get.json()
#     end_point = 'SEP/2.0/updtglplg'
#     method = 'put'
#     payload = data
#     return BpjsController.bridging(end_point,method,payload)

@app.route('/api/sep/pengajuansep',methods=['POST'])
def pengajuan_sep():
    no_kartu = request.form['no_kartu']
    tgl_sep = request.form['tglsep']
    jenis_pelayanan = request.form['jenis_pelayanan']
    jenis_pengajuan = request.form['jenis_pengajuan']
    keterangan = request.form['keterangan']
    user = request.form['user']
    end_point = 'Sep/pengajuanSEP'
    method = 'post'
    payload = {
        "request": {
            "t_sep": {
                "noKartu": no_kartu,
                "tglSep": tgl_sep,
                "jnsPelayanan": jenis_pelayanan,
                "jnsPengajuan": jenis_pengajuan,
                "keterangan": keterangan,
                "user": user
            }
        }
    }
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/sep/aprovalsep',methods=['POST'])
def aproval_sep():
    no_kartu = request.form['no_kartu']
    tgl_sep = request.form['tglsep']
    jenis_pelayanan = request.form['jenis_pelayanan']
    jenis_pengajuan = request.form['jenis_pengajuan']
    keterangan = request.form['keterangan']
    user = request.form['user']
    end_point = 'Sep/aprovalSEP'
    method = 'post'
    payload = {
        "request": {
            "t_sep": {
                "noKartu": no_kartu,
                "tglSep": tgl_sep,
                "jnsPelayanan": jenis_pelayanan,
                "jnsPengajuan": jenis_pengajuan,
                "keterangan": keterangan,
                "user": user
            }
        }
    }
    return BpjsController.bridging(end_point,method,payload)

@app.route('/api/sep/2.0/update_tanggal_pulang',methods=['POST'])
def update_tanggal_pulang():
    no_sep = request.form['no_sep']
    status_pulang = request.form['status_pulang']
    no_surat_meninggal = request.form['no_surat_meninggal']
    tgl_meninggal = request.form['tgl_meninggal']
    tgl_pulang = request.form['tgl_pulang']
    no_lp_manual = request.form['no_lp_manual']
    user = request.form['user']
    end_point = 'SEP/2.0/updtglplg'
    method = 'put'
    payload = {
        "request":{
            "t_sep":{
                "noSep": "0301R0110121V000829",
                "statusPulang":"4",
                "noSuratMeninggal":"325/K/KMT/X/2021",
                "tglMeninggal":"2021-02-10",
                "tglPulang":"2021-02-14",
                "noLPManual":"",
                "user":"coba"
                }
            }
        }
    return BpjsController.bridging(end_point,method,payload)


@app.route('/api/sep/kllinduk/list')
def kll_induk():
    no_kartu = request.args.get('noKartu')
    end_point = 'sep/KllInduk/List/'+no_kartu
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)