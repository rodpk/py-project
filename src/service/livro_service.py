from models.autor import Autor


class LivroService:
    def __init__(self) -> None:
        pass
    
    def run(self):
        autor = Autor("Rodrigo")
        print(autor)