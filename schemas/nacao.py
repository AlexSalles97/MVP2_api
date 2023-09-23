from pydantic import BaseModel
from typing import List

from model.nacao import Nacao


class NacaoSchema(BaseModel):
    """ Define como um novo país a ser inserido deve ser representado
    """
    pais: str = "Sallestão"
    continente: str = "América"
    lingua: str = "Sallesianismo"
    capital: str = "Sallesland"
    moeda: str = "XPNC"


class NacaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base na id do país.
    """
    id: int = 1


class UpdateNacaoByIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca para editar. Que será
        feita apenas com base no id do país.
    """
    id: int = 1


class NacaoBuscaDelSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca para deletar. Que será
        feita apenas com base no id do país.
    """
    id: int = 1


class NacaoViewSchema(BaseModel):
    """ Define como um país será retornado.
    """
    id: int = 1
    pais: str = "Sallestão"
    continente: str = "América"
    lingua: str = "Sallesianismo"
    capital: str = "Sallesland"
    moeda: str = "XPNC"


class ListarNacoesSchema(BaseModel):
    """ Define como uma listagem de países que será retornada.
    """
    nacoes:List[NacaoSchema]


class UpdateNacaoSchema(BaseModel):
    """ Define como um país a ser editado deve ser representado
    """
    pais: str = "Sallestão"
    continente: str = "América"
    lingua: str = "Sallesianismo"
    capital: str = "Sallesland"
    moeda: str = "XPNC"


class NacaoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    id: int


def apresenta_nacoes(nacoes: List[Nacao]):
    """ Retorna uma representação dos países seguindo o schema definido em
        NacaoViewSchema.
    """
    result = []
    for nacao in nacoes:
        result.append({
            "id": nacao.id,
            "pais": nacao.pais,
            "continente": nacao.continente,
            "lingua": nacao.lingua,
            "capital": nacao.capital,
            "moeda": nacao.moeda,
        })

    return {"nacoes": result}


def apresenta_nacao(nacao: Nacao):
    """ Retorna uma representação do país seguindo o schema definido em
        NacaoViewSchema.
    """
    return {
        "id": nacao.id,
        "pais": nacao.pais,
        "continente": nacao.continente,
        "lingua": nacao.lingua,
        "capital": nacao.capital,
        "moeda": nacao.moeda
    }

