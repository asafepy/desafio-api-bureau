from flask_restful import Resource
from base_c.core.db.manager import Manager
from base_c.core.utils import person_trail_serializer


class HistoricoList(Resource):
    def get(self, cpf):
        manager = Manager()
        historico = manager.get(cpf)

        if person_trail:
            return person_trail_serializer(person_trail)
        else:
            abort(404)


class HistoricoCreate(Resource):

    def post(self):
        manager = Manager()
        historico = manager.random_create([1,2,3,4,5])

        if person_trail:
            return historico_serializer(historico)
        else:
            abort(404)
