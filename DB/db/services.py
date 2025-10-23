from conexão_banco import conn
from conexão_banco import cursor
from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

var = sha256.hash(input)

sha256.verify(input,hash)

def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha)
        )
        conn.commit()
        print('Usuário cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()

        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')
            for u in usuarios:
                print(f'| {u}')
        else:
            print('Nenhum usuário encontrado!')

    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def excluir_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM TB_USUARIO WHERE ID=?
        """, (id,))
        
        conn.commit()


    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def editar_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def listar_usuario_email(email):
    try:
        conn = get_connet()
        cursor = conn.cursor()
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def listar_usuario_id(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def criar_tabela():
    try:
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

def cadastro_produto():
 try:
        ID = input('Digite o ID do produto: ').strip()
        Desc = input('Digite o nome do produto: ').strip().title()
        Pr = float(input('Digite o preço do produto: R$ ').strip())
        Quan = int(input('Digite a quantidade de produtos: ').strip())
        
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_PRODUTO(Identificacao, Descricao, Preco, Quantidade) VALUES (?, ?, ?, ?)',
                       (ID, Desc, Pr, Quan))
        conn.commit()
        conn.close()
        print('Produto cadastrado com sucesso!')
 except Exception as e:
        print(f' Falha ao cadastrar produto: {e}')

def listar_produto():
 try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT Identificação, Descrição, Preço, Quantidade SENHA FROM TB_PRODUTOS')
        produtos = cursor.fetchall()

        if produtos:
            print(f'{30*'-'}Lista de produtos!{30*'-'}')
            for u in produtos:
                print(f'| {u}')
        else:
            print('Nenhum produto encontrado!')
 except Exception as e:
        print(f'Falha ao cadastrar produto: {e}')


def editar_id_produto():
   try:
        id_antigo = input('Digite o ID atual do produto: ').strip()
        id_novo = input('Digite o novo ID do produto: ').strip()
        
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("UPDATE TB_PRODUTO SET Identificacao=? WHERE Identificacao=?", (id_novo, id_antigo))
        conn.commit()
        conn.close()
        print('ID do produto editado')
   except Exception as e:
        print(f' Falha ao editar ID do produto: {e}')


def editar_preço_produto():
    try:
        id_produto = input('Digite o ID do produto: ').strip()
        novo_preco = float(input('Digite o novo preço: R$ ').strip())
        
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("UPDATE TB_PRODUTO SET Preco=? WHERE Identificacao=?", (novo_preco, id_produto))
        conn.commit()
        conn.close()
        print('Preço do produto editado com sucesso!')
    except Exception as e:
        print(f'Falha ao editar preço do produto: {e}')


def editar_quantidade_produto():
    try:
        id_produto = input('Digite o ID do produto: ').strip()
        nova_quantidade = int(input('Digite a nova quantidade: ').strip())
        
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("UPDATE TB_PRODUTO SET Quantidade=? WHERE Identificacao=?", (nova_quantidade, id_produto))
        conn.commit()
        conn.close()
        print('Quantidade do produto editada')
    except Exception as e:
        print(f'Falha ao editar quantidade do produto: {e}')
   
def editar_produto():
    print('\n--- Editar Produto ---')
    print('1 - Editar id do produto.')
    print('2 - Editar preço do produto.')
    print('3 - Editar quantidade do produto.')
    print('4 - Encerrar  essa parte do programa.')
    op = input('Digite a opção que deseja selecionar: ').strip()

    match op:
     case '1':
      editar_id_produto()

     case '2':
      editar_preço_produto()

     case '3':
      editar_quantidade_produto()

     case '4':
      sair()

     
try:

  conn = get_connet()
  cursor = conn.cursor()
except Exception as e:
       print(f'Falha ao cadastrar produto: {e}')

def vender_produto():
 try:
        id_produto = input('Digite o ID do produto: ').strip()
        quantidade_venda = int(input('Digite a quantidade a vender: ').strip())
        
        conn = get_connet()
        cursor = conn.cursor()
        
        # Buscar quantidade atual
        cursor.execute("SELECT Quantidade FROM TB_PRODUTO WHERE Identificacao=?", (id_produto,))
        resultado = cursor.fetchone()
        
        if resultado:
            quantidade_atual = resultado[0]
            
            if quantidade_atual >= quantidade_venda:
                nova_quantidade = quantidade_atual - quantidade_venda
                cursor.execute("UPDATE TB_PRODUTO SET Quantidade=? WHERE Identificacao=?", 
                             (nova_quantidade, id_produto))
                conn.commit()
                print(f'Venda realizada! Quantidade restante: {nova_quantidade}')
            else:
                print(f'Estoque insuficiente! Disponível: {quantidade_atual}')
        else:
            print(' Produto não encontrado!')
        
        conn.close()
 except Exception as e:
        print(f'Falha ao vender produto: {e}')


  
def sair():
    exit()

if __name__ == '__main__':
    #criar_tabela()
    nome = input('Digite um nome: ').strip().title()
    email = input('Digite um email: ').strip()
    senha = input('Digite uma senha: ').strip()
    senha = sha256.hash(senha)
    print(senha)

    criar_usuario(nome, email, senha)
    listar_usuario()
    excluir_usuario(1) 
    excluir_usuario(2) 
    excluir_usuario(3) 


   
def interface():
    print('1 - Cadastrar Produto.')
    print('2 - Listar Produtos.')
    print('3 - Editar Produtos.')
    print('4 - Vender Produtos .')
    print('5 - Encerrar programa.')

    opcao = input('Digite a opção que deseja selecionar: ')

    match opcao:
     case '1':
      cadastro_produto()

     case '2':
      listar_produto()

     case '3':
      editar_produto()

     case '4':
      vender_produto()

     case '5':
        sair()