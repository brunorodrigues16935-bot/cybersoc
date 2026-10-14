
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "cybersoc.db"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao



def criar_tabela():
    with conectar() as conexao:
        # Tabela de logs
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT NOT NULL,
                usuario TEXT NOT NULL,
                status TEXT NOT NULL,
                horario TEXT NOT NULL
            )
        """)

        # Tabela de incidentes de segurança
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS incidentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT NOT NULL,
                risco TEXT NOT NULL,
                motivo TEXT NOT NULL,
                horario TEXT NOT NULL
            )
        """)
