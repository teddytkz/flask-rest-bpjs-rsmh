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
from app.model import bpjs_rencana_kontrol_response
from app.model import bpjs_rencana_ri_response
from app import routes