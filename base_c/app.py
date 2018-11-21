import json

from flask import Flask, abort
from flask_restful import Resource, Api

from base_c.core.views import HistoricoList, HistoricoGet, HistoricoCreate

app = Flask(__name__)
api = Api(app)

api.add_resource(HistoricoGet, '/historico/<string:cpf>')
api.add_resource(HistoricoList, '/historico')
api.add_resource(HistoricoCreate, '/historico/create')

if __name__ == '__main__':
    app.run(debug=True)