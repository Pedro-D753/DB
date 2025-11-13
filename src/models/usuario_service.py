from src.models.usuario_model import Usuario
from sqlalchemy.orm import Session

session = Session()

def criar_usuario(usuario):
    usuario_db = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)

    session.add(usuario_db)
    session.commit()
    return usuario_db

# QUERY - método de consulta
# FIRST - traz a primeira ocorrência
def listar_usuario_email(email):
    usuario_db = session.query(Usuario).filter(Usuario.email == email).first()
    return usuario_db

def listar_usuario_id(id):
    usuarios_db = session.query(Usuario).all()
    return usuarios_db

def excluir_usuario(id):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return False   

def editar_usuario(id, novo_nome, novo_email):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        usuario_db.nome = novo_nome
        usuario_db.email = novo_email
        session.commit()
        return usuario_db
    return False
    