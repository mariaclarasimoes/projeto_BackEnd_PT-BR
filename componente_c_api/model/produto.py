from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    classificacao = Column(Float)
    preco = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, classificacao: float, preco: float,data_insercao:Union[DateTime, None] = None):
        """ Cria um produto

        Arguments:
            *nome: Nome da produto.
            *classificacao: Classificação do produto dada pelos clientes
            *preço: Preço do produto
            *data_insercao: Data de compra do cliente (data de inserção no banco)
        """
        self.nome = nome
        self.classificacao = classificacao
        self.preco = preco

        # Data exata da inserção no banco.
        if data_insercao:
            self.data_insercao = data_insercao


