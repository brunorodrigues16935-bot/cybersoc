
from flask import Blueprint, render_template, request
from services.logs import obter_logs, contar_eventos


from services.logs import (
    obter_logs,
    contar_eventos,
    detectar_ips_suspeitos,
    obter_incidentes
)

dashboard_bp = Blueprint("dashboard", __name__)


# Página principal
@dashboard_bp.route("/")
def dashboard():
    logs = obter_logs()
    estatisticas = contar_eventos()

    return render_template(
        "index.html",
        logs=logs,
        falhas=estatisticas["falhas"],
        sucessos=estatisticas["sucessos"]
    )


@dashboard_bp.route("/logs")
def logs_acesso():
    ip = request.args.get("ip", "").strip()
    status = request.args.get("status", "").strip()

    registros = obter_logs()

    if ip:
        registros = [
            log for log in registros
            if ip.lower() in log["ip"].lower()
        ]

    if status in ("Falha", "Sucesso"):
        registros = [
            log for log in registros
            if log["status"] == status
        ]

    return render_template(
        "logs.html",
        logs=registros,
        filtro_ip=ip,
        filtro_status=status
    )



# Página de IPs suspeitos

@dashboard_bp.route("/ips-suspeitos")
def ips_suspeitos():
    suspeitos = detectar_ips_suspeitos()

    return render_template(
        "ips_suspeitos.html",
        suspeitos=suspeitos
    )

@dashboard_bp.route("/incidentes")
def historico_incidentes():
    incidentes = obter_incidentes()

    return render_template(
        "incidentes.html",
        incidentes=incidentes
    )
