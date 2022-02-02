from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app,db)

from app.model import bpjs_sep_response
from app.model import bpjs_sep_request
from app import routes



# if not hasattr(res, 'status_code'):
    #     return jsonify(res), 400
    # if res.status_code != 404:
    #     if check_json(res.text) == True:
    #         keys = consid + secret + timestamp
    #         res = res.json()
    #         metadata = 'metaData'
    #         if metadata not in res:
    #             metadata = 'metadata'
    #         code = 'code'
    #         if code not in res[metadata]:
    #             code = 'Code'
    #         if res[metadata][code] == 0:
    #             data = {
    #                 'metaData': {
    #                     'code': 400,
    #                     'message': res[metadata]['message'],
    #                 },
    #                 'response': None
    #             }
    #             return jsonify(data), 400
    #         if 'response' not in res:
    #             data = {
    #                 'metaData': {
    #                     'code': res[metadata][code],
    #                     'message': res[metadata]['message'],
    #                 },
    #                 'response': None
    #             }
    #             return jsonify(data), res[metadata][code]

    #         if int(is_encrypt) == 1:
    #             url_not_encrypt = ["SEP/2.0/delete", "SEP/2.0/update"]
    #             status_encrypt = True
    #             for unc in url_not_encrypt:
    #                 if unc in url:
    #                     status_encrypt = False

    #             if status_encrypt == True:
    #                 response = decrypt_data(keys, res['response'])

    #             else:
    #                 response = res['response']
    #         else:
    #             response = res['response']

    #         data = {
    #             'metaData': {
    #                 'code': res[metadata][code],
    #                 'message': res[metadata]['message'],
    #             },
    #             'response': response
    #         }

    #         status_code = res[metadata][code]

    #         if res[metadata][code] == 1:
    #             status_code = 200
                    
    #         return jsonify(data), status_code

    #     else:
    #         data = {
    #             'metaData': {
    #                 'code': res.status_code,
    #                 'message': res.text,
    #             },
    #             'response': None
    #         }
    #         return jsonify(data), res.status_code

    # else:
    #     data = {
    #         'metaData': {
    #             'code': 404,
    #             'message': "URL tidak ditemukan",
    #         },
    #         'response': None
    #     }

    #     return jsonify(data), 404