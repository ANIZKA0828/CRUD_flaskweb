from .views import index_view
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import create_view, detail_view, modify_view, delete_view
    app.register_blueprint(index_view.bp)
    app.register_blueprint(create_view.bp)
    app.register_blueprint(detail_view.bp)
    app.register_blueprint(modify_view.bp)
    app.register_blueprint(delete_view.bp)

    return app