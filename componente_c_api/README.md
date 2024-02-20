# MINHA API
Este projeto é o MVP (minimum viable product) para conclusão da disciplina "Back end Avançado" ofertado pela PUC-Rio.
O objetivo é colocar em prática o conteúdo apresentado ao longo das aulas explorando a ideia de componentes e microsserviços.

## COMO EXECUTAR A API

1) Instalar todas as libs python listadas no arquivo `requirements.txt`.

2) Após clonar o repositório, acessar o terminal e executar os comandos descritos abaixo:

    * Criar um ambiente virtual -> Comando no terminal: python -m venv env
    * Ativar o ambiente virtual ->  Comando no terminal PARA WINDOWS: .\env\Scripts\activate (Para MAC e LINUX é utilizado outro comando)
    * Instalar os requisitos -> Comando no terminal: pip install -r requirements.txt
      Se necessário, fazer a atualização utilizando o comando no terminal: python.exe -m pip install --upgrade pip
      
    * Executar a API utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 
      Comando no terminal: flask run --host 0.0.0.0 --port 5000 --reload
    * Abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## COMO EXECUTAR ATRAVÉS DO DOCKER

1) Certifique-se de ter o Docker instalado e em execução em sua máquina.

2) Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:
```
(env)$ docker build -t componente_c_api .
```

2) Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:
```
(env)$ docker run -p 5000:5000 componente_c_api
```

3) Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


