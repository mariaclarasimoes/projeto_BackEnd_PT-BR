from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Cliente
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição das tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    
    return redirect('/openapi')


@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados
    Retorna uma representação dos clientes associados. """

    cliente = Cliente(
        name=form.name,
        email=form.email,
        city=form.city,
        state=form.state,
        zip=form.zip
        )
    logger.debug(f"Adicionando um cliente de nome: '{cliente.name}'")
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando cliente
        session.add(cliente)
        # Efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.name}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # A duplicidade do name é provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome já salvo na base"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # Caso ocorra outro erro fora do previsto
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_clientes():
    """Faz a busca por todos os clientes cadastradas. 
    Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes")
    # Cria uma conexão com a base
    session = Session()
    # Faz a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # Checa se não há clientes cadastradas
        return {"Clientes": []}, 200
    else:
        logger.debug(f"%d clientes encontrados: " % len(clientes))
        # Retorna a representação da cliente
        print(clientes)
        return apresenta_clientes(clientes), 200

@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):
    """Faz a busca por um cliente a partir do id do registro

    Retorna uma representação dos clientes associados.
    """
    name = query.name
    logger.debug(f"Coletando dados sobre o cliente #{name}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.id == name).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base"
        logger.warning(f"Erro ao buscar cliente '{name}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente encontrado: '{cliente.name}'")
        # retorna a representação de cliente
        return apresenta_cliente(cliente), 200


@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_cliente(query: ClienteBuscaSchema):
    """Deleta um cliente a partir do "nome do cliente" informado
    Retorna uma mensagem de confirmação da remoção. """
    cliente_name = unquote(unquote(query.name))
    print(cliente_name)
    logger.debug(f"Deletando dados sobre a cliente #{cliente_name}")

    # Criando conexão com a base
    session = Session()

    # Faz a remoção
    count = session.query(Cliente).filter(Cliente.name == cliente_name).delete()
    session.commit()

    if count:
        # Retorna a representação da mensagem de confirmação
        logger.debug(f"Cliente deletado: #{cliente_name}")
        return {"mesage": "Cliente removido", "id": cliente_name}
    else:
        # Se o cliente não foi encontrada
        error_msg = "Cliente não encontrado na base"
        logger.warning(f"Erro ao deletar cliente #'{cliente_name}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.put('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_revisao_put(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados

    Retorna uma representação dos clientes associados.
    """
    cliente = Cliente(
        name=form.name,
        email=form.email,
        city=form.city,
        state=form.state,
        zip=form.zip)
    logger.debug(f"Adicionando cliente: '{cliente.name}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivando o camando de adição de novo registro na tabela
        session.commit()
        logger.debug(f"Adicionado cliente: '{cliente.name}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do name é a provável razão do IntegrityError
        error_msg = "Cliente já adicionado"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo registro"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"mesage": error_msg}, 400