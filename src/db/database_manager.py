## pip install cx_Oracle
import cx_Oracle


class DatabaseManager:
    def __init__(self) -> None:
        ## detalhes da conexao
        self.usuario = "SYSTEM"
        self.senha = "admin"
        self.host = "localhost"
        self.porta = "1521"
        self.sid = "XE"
        pass

    def criar_conexao(self):
        ## DSN (Data source name)
        dsn = cx_Oracle.makedsn(self.host, self.porta, sid=self.sid)

        conexao = cx_Oracle.connect(self.usuario, self.senha, dsn)

        return conexao

    ## close conn
