from flask import request, Flask

from api.common import db
from config import configs


app = Flask(__name__, instance_relative_config=True)


def create_app(config_name):
    # 解决current_app指向为空问题
    app.app_context().push()
    # 初始化db
    db.init_app(app)
    # 初始化sqlalchemy
    db.init_engine(app)
    # 加载配置文件
    app.config.from_object(configs[config_name])

    from api.controller.user import user_api
    app.register_blueprint(user_api, url_prefix='/user')

    return app