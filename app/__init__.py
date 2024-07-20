import os

from flask import Flask, render_template
from flask_login import current_user
from flask_wtf.csrf import CSRFError
import click

from app.views import main_bp
from app.config import config  # 导入存储配置的字典
from app.extensions import bootstrap, db, moment, csrf
from app.utils import fake_message

def create_app(config_name=None):
    if config_name is None:
        # 从环境变量中获取FLASK_ENV，并设置默认值，同时确保它是有效的配置名称
        config_name = os.getenv('FLASK_ENV', 'development')
        if config_name not in config:
            raise ValueError(f"Invalid config name: {config_name}. Must be one of {list(config.keys())}")

    app = Flask('app')

    # 导入配置，根据配置环境实例化对象
    app.config.from_object(config[config_name])

    # 注册扩展
    register_extensions(app)
    register_commands(app)
    register_blueprints(app)
    register_errors(app)

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)

def register_blueprints(app):
    app.register_blueprint(main_bp)

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error.html', description=e.description, code=e.code), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('error.html', description=e.description, code=e.code), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', description=e.description, code=e.code), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('error.html', description=e.description, code=e.code), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', description='Internal Server Error', code='500'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('error.html', description=e.description, code=e.code), 400
    
def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--count', default=20, help='Quantity of messages, default is 20.')
    def forge(count):
        """Generate fake messages."""
        fake_message(count)
        click.echo('Forged {} messages'.format(count))