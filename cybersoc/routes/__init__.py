from routes.dashboard import dashboard_bp
from routes.api import api_bp

def registrar_rotas(app):
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)
    