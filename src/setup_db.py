import sys
from db.database_manager import DatabaseManager


def ler_arquivo_sql(filename="create_tables.sql"): 
    with open(f'../scripts/{filename}', 'r', encoding="utf-8") as file:
        comandos_sql = file.read().split(";")
    return comandos_sql

def executar_sql(conn, comandos_sql):
    cursor = conn.cursor()
    for comando in comandos_sql:
        print("Linha atual: ", comando)
        if comando.strip(): # verifica se nao esta vazio
            if not comando.strip().startswith("--"):
                print("Executando o comando ", comando)
                cursor.execute(comando)
    
    conn.commit()
    cursor.close()
    
    print("Comandos executados com sucesso")
    pass



db_manager = DatabaseManager()
conn = db_manager.criar_conexao()

opcao = int(input("1. Inicializar banco de dados\n2. Limpar banco de dados\n"))

if opcao == 1: 
    comandos_sql = ler_arquivo_sql("create_tables.sql")
elif opcao == 2:
    comandos_sql = ler_arquivo_sql("drop_tables.sql")
else:
    print("Opcao invalida")
    
    
executar_sql(conn, comandos_sql)
conn.close()

