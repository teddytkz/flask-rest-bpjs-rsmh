from app import app
from flask import Flask,request,jsonify
from datetime import datetime

from app.controller import BpjsController
from app.controller import DataController

@app.route('/api/monitoring/historypelayanan',methods=['GET'])
def monitoring_history_pelayanan():
    no_kartu = request.args.get('no_kartu')
    tgl_mulai = request.args.get('tgl_mulai')
    tgl_akhir = request.args.get('tgl_akhir')
    end_point = 'monitoring/HistoriPelayanan/NoKartu/'+no_kartu+'/tglMulai/'+tgl_mulai+'/tglAkhir'+tgl_akhir
    method = 'get'
    payload = ''
    return BpjsController.bridging(end_point,method,payload)
