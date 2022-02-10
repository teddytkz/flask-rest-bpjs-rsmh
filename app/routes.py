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
from app.router import peserta_router
from app.router import referensi_router
from app.router import rujukan_router

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








