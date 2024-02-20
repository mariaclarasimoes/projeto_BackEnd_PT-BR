from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto



class ProdutoSchema(BaseModel):
    # Define como os campos devem ser representados ao inserir um novo produto.
    
    nome: str = "Mens Casual Slim Fit"
    classificacao: float = "2.1"
    preco: float = "15.99"

    
class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca que será feita apenas com base no "id" do produto. """
    
    nome: str = "Boné"


class ListagemProdutosSchema(BaseModel):
    # Define como uma listagem de produtos será retornada.

    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    # Retorna a representação da produto seguindo o schema definido em "ProdutoViewSchema".
  
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "classificacao": produto.classificacao,
            "preco": produto.preco,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    # Define como um produto será retornado.

    id: int = 1
    nome: str = "Mens Casual Slim Fit"
    classificacao: float = "4.1"
    preco: float = "22.9"


class ProdutoDelSchema(BaseModel):
    # Define como deve ser a estrutura do dado retornado após uma requisição de remoção.

    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    # Retorna uma representação do produto seguindo o schema definido em ProdutoViewSchema.

    return {
        "id": produto.id,
        "nome": produto.nome,
        "classificacao": produto.classificacao,
        "preco": produto.preco,
    }
