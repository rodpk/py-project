import cx_Oracle

from models.autor import Autor


class AutorRepository:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.cursor = self.conn.cursor()

    def inserir_autor(self, autor: Autor):
        query = "INSERT INTO AUTORES (NOME, NACIONALIDADE) VALUES (:1, :2)"
        self.cursor.execute(
            query, (autor.nome, autor.nacionalidade)
        )
        self.conn.commit()

    def listar_autores(self):
        self.cursor.execute("SELECT * FROM AUTORES")
        return self.cursor.fetchall()

    def atualizar_autor(self, id, autor: Autor):
        query = "UPDATE AUTORES SET NOME = :1, NACIONALIDADE = :2 WHERE ID = :3"
        self.cursor.execute(
            query, (autor.nome, autor.nacionalidade, id)
        )
        self.conn.commit()

    def deletar_autor(self, id):
        query = "DELETE FROM AUTORES WHERE ID = :1"
        self.cursor.execute(query, id)
        self.conn.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

    def pegar_contagem_autores(self):
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM AUTORES"
        cursor.execute(query)
        contagem = cursor.fetchone()[0]
        cursor.close()
        return contagem
