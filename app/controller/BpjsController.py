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

app = Flask(__name__)
cors = CORS(app)

config = dotenv_values(".env")
host = config['BPJS_HOST']
consid = config['BPJS_CONST_ID']
secret = config['BPJS_SECRET_KEY']
user_key = config['BPJS_USER_KEY']
is_encrypt = config['IS_ENCRYPT']

def test():
    return 'Hello World'

def bridging_new(end_point,method,payload):
    url = host+end_point
    res = rest_bpjs(url,method,payload)
    keys = consid + secret + timestamp
    res = res.json()
    metadata='metaData'
    code='code'
    response = decrypt_data(keys,res['response'])
    data = {
        'metaData':{
            'code':res[metadata][code],
            'message':res[metadata]['message']
        },
        'response':response
    }
    status_code = res[metadata][code]
    # return jsonify(data),status_code
    return res

def bridging_data(end_point,method,payload):
    timestamp = str(int(datetime.today().timestamp()))
    url = host+end_point
    res = rest_bpjs(url,method,payload,timestamp)
    keys = consid + secret + timestamp
    res = res.json()
    metadata='metaData'
    code='code'
    url_not_encrypt = ['SEP/2.0/delete',"SEP/2.0/update"]
    status_encrypt = True
    for unc in url_not_encrypt:
        if unc in url:
            status_encrypt = False
    if status_encrypt == True:
        response = decrypt_data(keys,res['response'])
    else:
        response = res['response']
    
    data = {
        'metaData':{
            'code':res[metadata][code],
            'message':res[metadata]['message']
        },
        'response':response
    }
    status_code = res[metadata][code]
    return data

def bridging(end_point,method,payload):
    timestamp = str(int(datetime.today().timestamp()))
    url = host+end_point
    res = rest_bpjs(url,method,payload,timestamp)
    keys = consid + secret + timestamp
    res = res.json()
    metadata='metaData'
    code='code'
    url_not_encrypt = ['SEP/2.0/delete',"SEP/2.0/update"]
    status_encrypt = True
    for unc in url_not_encrypt:
        if unc in url:
            status_encrypt = False
    if status_encrypt == True:
        response = decrypt_data(keys,res['response'])
    else:
        response = res['response']
    
    data = {
        'metaData':{
            'code':res[metadata][code],
            'message':res[metadata]['message']
        },
        'response':response
    }
    status_code = res[metadata][code]
    return jsonify(data),status_code

def rest_bpjs(url,method,payload,timestamp):
    message = consid+"&"+timestamp
    signature = hmac.new(bytes(secret,'UTF-8'),bytes(message,'UTF-8'), hashlib.sha256).digest()
    encodeSignature = base64.b64encode(signature)
    headers = {
        'X-cons-id': consid, 
        'X-timestamp': timestamp, 
        'X-signature': encodeSignature.decode('UTF-8'), 
        'user_key': user_key, 
        'Content-Type': 'Application/x-www-form-urlencoded',
        'Accept': '*/*'
    }
    if payload == '' or payload == None:
        payload = 0
    else:
        payload = json.dumps(payload)
    try:
        if method.lower() == 'post':
            if payload == 0:
                res = requests.post(url, headers=headers)
            else:
                res = requests.post(url, data=payload, headers=headers)
        elif method.lower() == 'put':
            if payload == 0:
                res = requests.put(url, headers=headers)
            else:
                res = requests.put(url, data=payload, headers=headers)
        elif method.lower() == 'delete':
            if payload == 0:
                res = requests.delete(url, headers=headers)
            else:
                res = requests.delete(url, data=payload, headers=headers)
        else:
            if payload == 0:
                res = requests.get(url, headers=headers)
            else:
                res = requests.get(url, data=payload, headers=headers)
    except:
        res = {
            'metaData': {
                'code': "400",
                'message': "Ada kesalahan request data, cek kembali",
            },
            'response': None
        }
    return res


def check_json(str_json):
    try:
        json_object = json.loads(str_json)
    except ValueError as e:
        return False
    return True

def decrypt_data(keys, encrypts):
    decompress = None
    if encrypts != None:
        x = lzstring.LZString()
        key_hash = hashlib.sha256(keys.encode('utf-8')).digest()
        decryptor = AES.new(key_hash[0:32], AES.MODE_CBC, IV=key_hash[0:16])
        plain = decryptor.decrypt(base64.b64decode(encrypts))
        decompress = json.loads(x.decompressFromEncodedURIComponent(plain.decode('utf-8')))
    return decompress
