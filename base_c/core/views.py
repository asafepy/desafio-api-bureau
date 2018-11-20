from flask_restful import Resource
from base_c.core.db.manager import Manager
from base_c.core.serializers import HistoricoSerializer

class HistoricoList(Resource):
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
