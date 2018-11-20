from pymodm import fields, MongoModel, EmbeddedMongoModel


class Pessoa(MongoModel):
    cpf = fields.CharField(primary_key=True)
    ultima_consulta = fields.DateTimeField()
    transacoes = fields.EmbeddedDocumentListField('Transacao')
    ultima_compra = fields.EmbeddedDocumentField('UltimaCompra')


class Transacao(EmbeddedMongoModel):
    data = fields.DateTimeField()
    valor = fields.FloatField(min_value=0)


class UltimaCompra(EmbeddedMongoModel):
    empresa = fields.CharField()
    data = fields.DateTimeField()
    valor = fields.FloatField(min_value=0)