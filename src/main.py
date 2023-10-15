import datetime
from db.livro_repository import LivroRepository
from models.autor import Autor
from db.autor_repository import AutorRepository
from db.database_manager import DatabaseManager
from service.livro_service import LivroService
from utils.tela_inicial import TelaInicial


db_manager = DatabaseManager()
conn = db_manager.criar_conexao()
autores_repository = AutorRepository(conn)
livros_repository = LivroRepository(conn)

tela_inicial = TelaInicial(livros_repository, autores_repository)
tela_inicial.mostrar_tela()
    
    



novo_autor = Autor(
    nome="Carlos Drummond de Andrade",
    nacionalidade="Brasileiro",
)

autores_repository.inserir_autor(novo_autor)
res = autores_repository.listar_autores()

print("Autores: ", res)
