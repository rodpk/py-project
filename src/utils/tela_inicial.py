import os
from time import sleep
from db.autor_repository import AutorRepository
from db.livro_repository import LivroRepository


class TelaInicial:
    def __init__(
        self, livros_repository: LivroRepository, autores_repository: AutorRepository
    ):
        ## pegando contagem de livros e autores
        self.qtdLivros = livros_repository.pegar_contagem_livros()
        self.qtdAutores = autores_repository.pegar_contagem_autores()
        ##

        self.criado_por = "rodpk"
        self.professor = "Howard Roatti"
        self.disciplina = "Banco de dados"
        self.semestre = "2023/2"
        pass

    def mostrar_tela(self):
        print(
            f"""
            Biblioteca
            
            Total de Registros:
            | Livros  | {self.qtdLivros}  |
            | Autores | {self.qtdAutores} |
            
            Criado por: {self.criado_por}
            Professor: {self.professor}
            Disciplina: {self.disciplina} - {self.semestre}

        """
        )

        sleep(3)
        os.system("clear")
