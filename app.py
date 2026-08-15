from flask import Flask
from configuration import init_db
from controller import patient_bp, agent_bp

def create_app(config_override=None):
    app = Flask(__name__)
    if config_override:
        app.config.update(config_override)
    init_db(app)

    app.register_blueprint(patient_bp)
    app.register_blueprint(agent_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)