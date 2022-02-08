from app import app

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
    data = request.get_json()
    end_point='SEP/2.0/delete'
    method = 'delete'
    payload = data
    return BpjsController.bridging(end_point,method,payload)