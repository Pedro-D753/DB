import sqlite3

def get_connect():
    try:
        conexao = sqlite3.connect('controle_usuario.db') 
        print('Conexão bem sucedida!')
        return conexao
    
    except sqlite3.Error as e:
        print('Falaha na conexão.', e)
        return None
    

if __name__=='__main__':
    get_connect()