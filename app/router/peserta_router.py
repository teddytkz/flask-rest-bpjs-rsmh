from app import app
from flask import Flask,request,jsonify
from datetime import datetime

from app.controller import BpjsController
from app.controller import DataController

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