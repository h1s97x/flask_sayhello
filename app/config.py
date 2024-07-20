import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 基础配置，使用继承的方式
class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data.db')

class DevelopmentConfig(BaseConfig):
    """
    开发环境
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    生产环境
    """
    DEBUG = False


class TestingConfig(BaseConfig):
    """
    测试环境
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    # 在测试环境中，使用内存数据库
    USE_SQLITE = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database
    
# 映射环境对象
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

