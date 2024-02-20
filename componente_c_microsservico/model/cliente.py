from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    email = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    zip = Column(String(50))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, name:str, email: str, city: str, state: str, zip: str,
                 data_insercao:Union[DateTime, None] = None):
        """ Cria um cliente

        Arguments:
            *name: Nome do cliente.
            *email: Email do cliente.
            *city: Cidade em que o cliente reside.
            *State: Estado em que o cliente reside.
            *ZIP: ZIP CODE do local em que o cliente reside.
            *data_insercao: Data de compra do cliente (data de inserção no banco)
        """
        self.name = name
        self.email = email
        self.city = city
        self.state = state
        self.zip = zip

        # Data exata da inserção no banco.
        if data_insercao:
            self.data_insercao = data_insercao


