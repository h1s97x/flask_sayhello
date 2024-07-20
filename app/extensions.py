from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
csrf = CSRFProtect()
