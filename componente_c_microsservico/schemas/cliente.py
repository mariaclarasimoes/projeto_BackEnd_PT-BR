from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente



class ClienteSchema(BaseModel):
    # Define como os campos devem ser representados ao inserir um novo cliente.
    
    name: str = "George Smith"
    email: str = "george.smith@example.com"
    city: str = "Manhattan"
    state: str = "Nova York"
    zip: str = "10001"


    
class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca que será feita apenas com base no "id" do cliente. """
    
    name: str = "Ex: 1"


class ListagemClientesSchema(BaseModel):
    # Define como uma listagem de clientes será retornada.

    clientes:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    # Retorna a representação do cliente seguindo o schema definido em "ClienteViewSchema".
  
    result = []
    for cliente in clientes:
        result.append({
            "name": cliente.name,
            "email": cliente.email,
            "city": cliente.city,
            "state": cliente.state,
            "zip": cliente.zip,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    # Define como um cliente será retornado.

    id: int = 1
    name: str = "George Smith"
    email: str = "george.smith@example.com"
    city: str = "Manhattan"
    state: str = "Nova York"
    zip: str = "10001"


class ClienteDelSchema(BaseModel):
    # Define como deve ser a estrutura do dado retornado após uma requisição de remoção.

    mesage: str
    name: str

def apresenta_cliente(cliente: Cliente):
    # Retorna uma representação do cliente seguindo o schema definido em ClienteViewSchema.

    return {
        "id": cliente.id,
        "name": cliente.name,
        "email": cliente.email,
        "city": cliente.city,
        "state": cliente.state,
        "zip": cliente.zip,
    }
