
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database.db import initialize_db
from handlers.routes import configure_routes



app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'mongodb',
}

initialize_db(app)

api = Api(app)

CORS(app)

configure_routes(api, app)




