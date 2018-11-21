from flask_restful import Resource
from core.db.manager import Manager
from core.serializers import HistoricoSerializer
from flask import Flask, abort

class HistoricoList(Resource):
    def get(self):
        manager = Manager()
        historico = manager.all()

        if historico:
            return HistoricoSerializer(historico).data()
        else:
            abort(404)

class HistoricoGet(Resource):
    def get(self, cpf):
        manager = Manager()
        historico = manager.get(cpf)

        if historico:
            return HistoricoSerializer(historico).data()
        else:
            abort(404)


class HistoricoCreate(Resource):

    def post(self):
        manager = Manager()
        historico = manager.random_create([1,2,3,4,5])

        if historico:
            return HistoricoSerializer(historico).data()
        else:
            abort(404)
