
from flask import Blueprint, jsonify
from services.logs import obter_logs, contar_eventos, gerar_evento

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/logs")
def logs():
    estatisticas = contar_eventos()
    registros = obter_logs()

    return jsonify({
        "logs": registros,
        "falhas": estatisticas["falhas"],
        "sucessos": estatisticas["sucessos"],
        "ips": len(set(log["ip"] for log in registros))
    })


@api_bp.route("/gerar", methods=["POST"])
def gerar():
    novo_log = gerar_evento()
    return jsonify(novo_log), 201
