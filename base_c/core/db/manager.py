import random

from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_generator

from .conn import get_connection
from .models import Pessoa, Transacao, UltimaCompra
from base_c.core.utils import (name_generator, address_generator,
                          company_generator, value_generator,
                          status_generator, contract_generator,
                          date_generator)


class Manager(object):
    def __init__(self, *args, **kwargs):
        get_connection()

    def detele(self):
        Pessoa.objects.all().delete()

    def get(self, cpf):
        return Pessoa.objects.raw({'_id':cpf}).first()
    
    def random_create(self, id_list):
        for person_info in id_list:
            ultima_compra = UltimaCompra(   
                empresa=company_generator(),
                data=date_generator(),
                valor=value_generator()
            )

            transactions = []
            for _ in range(3):
                transactions.append(Transacao(
                    data=date_generator(),
                    valor=value_generator()
                ))

            Pessoa(
                cpf=person_info,
                ultima_consulta=date_generator(),
                transacoes=transactions,
                ultima_compra=ultima_compra
            ).save()