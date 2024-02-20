# MEU FRONT END

Este projeto faz parte da conclusão do MVP da disciplina **Back end avançado** 

# API EXTERNA

* Foi utilizada a api externa do website https://fakestoreapi.com
* É API externa pública de produtos para abastecer as informações da loja online.
* Rota que será utilizada: GET.
* Não é necessário ter licença de uso, pagar ou fazer cadastro.

## COMO EXECUTAR

Basta fazer o download do projeto e abrir o arquivo index.html no seu browser.

## COMO EXECUTAR ATRAVÉS DO DOCKER

1) Certifique-se de ter o Docker instalado e em execução em sua máquina.

2) Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:
```
$ docker build -t componente_a .
```

3) Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:
```
(env)$ docker run -d -p 8080:80 componente_a