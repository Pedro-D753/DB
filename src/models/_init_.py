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

Base.metadata.create_all(engine)

"""
# Criando uma tabela  
class Usuario(Base):
    __tablename__ = 'usuarios'

id = Column(Integer, primary_key=True)
nome = Column(String)
idade = Column(Integer)


#Criação de sessão
Session = sessionmaker(bind=engine)
session = Session()

#Criação do usuário
novo_usuario = Usuario(nome="Alice", idade=30)

#Adicionar e salvaar no banco
session.add(novo_usuario)
session.commit()

#Buscando usuários
usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario)

"""