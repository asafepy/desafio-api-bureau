import json
import datetime

class HistoricoSerializer:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def data(self):
        data = self.pessoa.to_son().to_dict()
        return json.loads(json.dumps(data, default=self.datetime_serializer))


    def datetime_serializer(self, obj):
        print(obj)
        if isinstance(obj, datetime.datetime):
            return datetime.datetime