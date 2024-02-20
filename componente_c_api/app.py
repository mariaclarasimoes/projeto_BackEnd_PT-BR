from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição das tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo produto à base de dados
    Retorna uma representação dos produtos associados. """

    produto = Produto(
        nome=form.nome,
        classificacao=form.classificacao,
        preco=form.preco
        )
    logger.debug(f"Adicionando um produto de nome: '{produto.nome}'")
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando produto
        session.add(produto)
        # Efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # A duplicidade do nome é provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # Caso ocorra outro erro fora do previsto
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os produtos cadastradas. 
    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos")
    # Cria uma conexão com a base
    session = Session()
    # Faz a busca
    produtos = session.query(Produto).all()

    if not produtos:
        # Checa se não há produtos cadastradas
        return {"Produtos": []}, 200
    else:
        logger.debug(f"%d produtos encontrados: " % len(produtos))
        # Retorna a representação da produto
        print(produtos)
        return apresenta_produtos(produtos), 200

@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um produto a partir do id do registro

    Retorna uma representação dos produtos associados.
    """
    nome = query.nome
    logger.debug(f"Coletando dados sobre o produto #{nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.id == nome).first()

    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base"
        logger.warning(f"Erro ao buscar produto '{nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto encontrado: '{produto.nome}'")
        # retorna a representação de produto
        return apresenta_produto(produto), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um produto a partir do "nome do produto" informado
    Retorna uma mensagem de confirmação da remoção. """
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre a produto #{produto_nome}")

    # Criando conexão com a base
    session = Session()

    # Faz a remoção
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if count:
        # Retorna a representação da mensagem de confirmação
        logger.debug(f"Produto deletado: #{produto_nome}")
        return {"mesage": "Produto removido", "id": produto_nome}
    else:
        # Se o produto não foi encontrada
        error_msg = "Produto não encontrado na base"
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.put('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_revisao_put(form: ProdutoSchema):
    """Adiciona um novo produto à base de dados

    Retorna uma representação dos produtos associados.
    """
    produto = Produto(
        nome=form.nome,
        classificacao=form.classificacao,
        preco=form.preco)
    logger.debug(f"Adicionando produto: '{produto.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo registro na tabela
        session.commit()
        logger.debug(f"Adicionado produto: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto já adicionado"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo registro"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400