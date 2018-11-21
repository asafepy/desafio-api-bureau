import random

from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_fake

from .conn import get_connection
from .models import Pessoa, Transacao, UltimaCompra
from base_c.core.utils import (name_fake, address_fake,
                               company_fake, value_fake,
                               status_fake, contract_fake,
                               date_fake)


class Manager:

    def __init__(self):
        get_connection()

    def all(self):
        return list(Pessoa.objects.values().all())

    def get(self, cpf):
        return Pessoa.objects.values().get({'_id':cpf})

    def detele(self):
        Pessoa.objects.all().delete()
    
    def random_create(self, lista_cpf):
        for person_info in lista_cpf:
            ultima_compra = UltimaCompra(   
                empresa=company_fake(),
                data=date_fake(),
                valor=value_fake()
            )

            transacoes = []
            for _ in range(3):
                transacoes.append(Transacao(
                    data=date_fake(),
                    valor=value_fake()
                ))

            Pessoa(
                cpf=person_info,
                ultima_consulta=date_fake(),
                transacoes=transacoes,
                ultima_compra=ultima_compra
            ).save()