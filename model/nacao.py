from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from typing import Union

from model import Base

class Nacao(Base):
    __tablename__ = 'nacao'

    id = Column("pk_nacao", Integer, primary_key=True)
    pais = Column(String(100), unique=True)
    continente = Column(String(100))
    lingua = Column(String(100))
    capital = Column(String(100))
    moeda = Column(String(100))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, pais:str, continente:str, lingua:str, capital:str, moeda:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria a tabela Nação

        Arguments:
            pais: nome do país
            continente: continente onde o país está localizado
            lingua: lingua oficial do país
            capital: capital do país
            moeda: moeda utilizada no país
            data_insercao: data de quando o país foi inserido à base
        """
        self.pais = pais
        self.continente = continente
        self.lingua = lingua
        self.capital = capital
        self.moeda = moeda

        # se não for informada, será a data exata da inserção no banco de dados
        if data_insercao:
            self.data_insercao = data_insercao