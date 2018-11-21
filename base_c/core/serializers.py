import json
import datetime

class HistoricoSerializer:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def data(self):
        data = self.pessoa
        return json.loads(json.dumps(data, default=self.datetime_serializer))


    def datetime_serializer(self, obj):
        if isinstance(obj, datetime.datetime):
            return datetime.datetime