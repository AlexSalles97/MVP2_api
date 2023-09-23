## 💻 Projeto API

Projeto de uma API simples desenvolvido por Alecsander Jesus Salles para o MVP da Sprint 2 da pós-graduação em Desenvolvimento Full Stack da PUC-Rio.

A seguinte API foi implementada com 5 rotas, um script com a tabela que será criada no banco de dados e a documentação com OpenAPI.

## 🚀 Tecnologias

Algumas das seguintes tecnologias utilizadas foram:

- Flask
- Python
- SQLite
- Swagger
- Docker
- Git e Github

## ⚒️ Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Em seguida é necessário ir ao diretório raiz, pelo terminal, e executar os comandos descritos abaixo.

```
py -m pip install --upgrade pip
```

> Este comando faz a instalação do pip.

```
py -m pip install --user virtualenv
```

> Este comando instala o ambiente virtual do tipo [virtualenv].

```
py -m venv env
```

> Este comando cria o ambiente virtual.

```
.\env\Scripts\activate
```

> Este comando ativa o ambiente virtual.

```
(env)$ py -m pip install -r requirements.txt
```

> Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Em seguida basta executar a API com o seguinte comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---
## ⚡ Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t back .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 back
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.