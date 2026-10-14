
import random
from datetime import datetime

from services.database import conectar, criar_tabela


# Cria a tabela caso ainda não exista
criar_tabela()

IPS_TESTE = [
    "192.0.2.10",
    "192.0.2.20",
    "192.0.2.30"
]


def gerar_evento():
    ip = random.choice(IPS_TESTE)

    if ip == "192.0.2.10":
        status = random.choice([
            "Falha", "Falha", "Falha", "Sucesso"
        ])
    else:
        status = random.choice(["Falha", "Sucesso"])

    usuario = random.choice([
        "admin", "bruno", "suporte", "guest"
    ])

    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with conectar() as conexao:
        cursor = conexao.execute(
            """
            INSERT INTO logs (ip, usuario, status, horario)
            VALUES (?, ?, ?, ?)
            """,
            (ip, usuario, status, horario)
        )

        novo_log = {
            "id": cursor.lastrowid,
            "ip": ip,
            "usuario": usuario,
            "status": status,
            "horario": horario
        }

    return novo_log


def obter_logs():
    with conectar() as conexao:
        registros = conexao.execute(
            """
            SELECT id, ip, usuario, status, horario
            FROM logs
            ORDER BY id DESC
            LIMIT 50
            """
        ).fetchall()

    return [dict(log) for log in registros]


def contar_eventos():
    with conectar() as conexao:
        resultado = conexao.execute(
            """
            SELECT
                SUM(CASE WHEN status = 'Falha' THEN 1 ELSE 0 END) AS falhas,
                SUM(CASE WHEN status = 'Sucesso' THEN 1 ELSE 0 END) AS sucessos
            FROM logs
            """
        ).fetchone()

    return {
        "falhas": resultado["falhas"] or 0,
        "sucessos": resultado["sucessos"] or 0
        
    }


def detectar_ips_suspeitos():
    with conectar() as conexao:
        registros = conexao.execute(
            """
            SELECT
                ip,
                COUNT(*) AS total_falhas
            FROM logs
            WHERE status = 'Falha'
            GROUP BY ip
            HAVING COUNT(*) >= 3
            ORDER BY total_falhas DESC
            """
        ).fetchall()

    suspeitos = []

    for registro in registros:
        total = registro["total_falhas"]

        if total >= 6:
            risco = "Alto"
        elif total >= 3:
            risco = "Medio"
        else:
            risco = "Baixo"

        suspeitos.append({
            "ip": registro["ip"],
            "total_falhas": total,
            "risco": risco
        })

    return suspeitos


def registrar_incidentes():
    suspeitos = detectar_ips_suspeitos()

    with conectar() as conexao:
        for suspeito in suspeitos:
            if suspeito["risco"] != "Alto":
                continue

            ip = suspeito["ip"]
            risco = suspeito["risco"]
            motivo = (
                f'{suspeito["total_falhas"]} tentativas '
                'de login falhas registradas'
            )

            # Evita registrar novamente o mesmo incidente
            # enquanto já existir um registro para esse IP.
            existente = conexao.execute(
                """
                SELECT id
                FROM incidentes
                WHERE ip = ? AND risco = ?
                LIMIT 1
                """,
                (ip, risco)
            ).fetchone()

            if existente:
                continue

            horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            conexao.execute(
                """
                INSERT INTO incidentes (ip, risco, motivo, horario)
                VALUES (?, ?, ?, ?)
                """,
                (ip, risco, motivo, horario)
            )

def obter_incidentes():
    with conectar() as conexao:
        registros = conexao.execute(
            """
            SELECT id, ip, risco, motivo, horario
            FROM incidentes
            ORDER BY id DESC
            """
        ).fetchall()

    return [dict(registro) for registro in registros]



