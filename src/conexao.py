from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'sqlite:///controle_usuario.db'

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    conntion = engine.connect()
    print('Banco conectado com sucesso!')
except Exception as e:
    print('Erro ao conectar ao banco')

# Classe base para os modelos
Base = declarative_base()