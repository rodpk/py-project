import cx_Oracle

class LivroRepository:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.cursor = self.conn.cursor()
        
    def pegar_contagem_livros(self):
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM LIVROS"
        cursor.execute(query)
        contagem = cursor.fetchone()[0]
        cursor.close()
        return contagem
