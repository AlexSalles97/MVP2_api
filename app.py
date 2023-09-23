from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from model import Session, Nacao
from schemas import *

info = Info(title="Api Países", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definição de tags
home_tag = Tag(name="Documentação", description="Seleção de Documentação: Swagger, Redoc ou RapiDoc")
nacao_tag = Tag(name="Nação", description="Adição, visualização e remoção de países à base de dados")

@app.get('/', tags=[home_tag])
def home():
    """Faz o redirecionamento para /openapi, tela onde permite a escolha de documentação.
    """
    return redirect('/openapi')

@app.post('/nacao', tags=[nacao_tag],
          responses={"200": NacaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_nacao(form: NacaoSchema):
    """Realiza a adição de um novo país à base de dados.
    
    Faz o retorno de uma representação dos países.
    """
    nacao = Nacao(
        pais=form.pais,
        continente=form.continente,
        lingua=form.lingua,
        capital=form.capital,
        moeda=form.moeda)

    try:
        # Realiza a conexão com a base.
        session = Session()
        # Adiciona o país.
        session.add(nacao)
        # Efetiva o comando de adição do novo país na tabela.
        session.commit()
        return apresenta_nacao(nacao), 200
 
    except IntegrityError as e:
        # A duplicidade do país é o motivo do IntegrityError.
        error_msg = "País de mesmo nome já salvo na base :/"
        return {"message": error_msg}, 409

    except Exception as e:
        # Erro imprevisivel.
        error_msg = "Não foi possível salvar novo país :/"
        return {"message": error_msg}, 400

@app.get('/nacoes', tags=[nacao_tag],
         responses={"200": ListarNacoesSchema, "404": ErrorSchema})
def get_nacoes():
    """Realiza a busca por todos os países cadastrados.
    
    Faz o retorno da listagem de países.
    """
    # Realiza a conexão com a base.
    session = Session()
    # Faz a busca.
    nacoes = session.query(Nacao).all()

    if not nacoes:
        # Se não há países cadastrados.
        return {"nacoes": []}, 200
    else:
        # Retorna a representação de países.
        print(nacoes)
        return apresenta_nacoes(nacoes), 200
  
@app.get('/nacao', tags=[nacao_tag],
         responses={"200": NacaoViewSchema, "404": ErrorSchema})
def get_nacao(query: NacaoBuscaSchema):
    """Realiza a busca por uma país a partir do id.
    
    Faz o retorno de uma representação do país.
    """
    nacao_id = query.id
    # Realiza a conexão com a base.
    session = Session()
    # Faz a busca.
    nacao = session.query(Nacao).filter(Nacao.id == nacao_id).first()

    if not nacao:
        # Quando o país não é encontrado.
        error_msg = "Pais não encontrado na base :/"
        return {"message": error_msg}, 404
    else:
        # Retorna a representação do país.
        return apresenta_nacao(nacao), 200

@app.put('/nacao', tags=[nacao_tag], 
            responses={"200": UpdateNacaoSchema, "404": ErrorSchema})
def update_nacao(query: UpdateNacaoByIdSchema, form: UpdateNacaoSchema):
    """
    Faz a busca por um país a partir do id do país, edita e retorna uma representação do país.
    """
    nacao_id = query.id
    # Realiza a conexão com a base.
    session = Session()
    # Faz a busca.
    nacao = session.query(Nacao).filter(Nacao.id == nacao_id).first()

    if not nacao:
        # Quando o país não é encontrado.
        error_msg = "País não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:        
        nacao.pais=form.pais
        nacao.continente=form.continente
        nacao.lingua=form.lingua
        nacao.capital=form.capital
        nacao.moeda=form.moeda

    try:
        # Efetiva o comando de adição do novo país na tabela.
        session.commit()
        return apresenta_nacao(nacao), 200
    
    except IntegrityError as e:
        # A duplicidade do país é o motivo do IntegrityError.
        error_msg = "Erro ao editar país :/"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        # Erro imprevisivel.
        error_msg = "Não foi possível editar o país :/"
        return {"mesage": error_msg}, 400

@app.delete('/nacao', tags=[nacao_tag],
            responses={"200": NacaoDelSchema, "404": ErrorSchema})
def del_nacao(query: NacaoBuscaDelSchema):
    """Realiza a exclusão de um país a partir do id informado.
    
    Faz o retorno de uma mensagem de confirmação de exclusão.
    """
    nacao_id = query.id
    print(nacao_id)
    # Realiza a conexão com a base.
    session = Session()
    # Exclui o país.
    count = session.query(Nacao).filter(Nacao.id == nacao_id).delete()
    session.commit()

    if count:
        # Retorna a representação da mensagem de confirmação.
        return {"message": "País removido", "id": nacao_id}
    else:
        # Quando o país não é encontrado.
        error_msg = "País não encontrado na base :/"
        return {"message": error_msg}, 404
