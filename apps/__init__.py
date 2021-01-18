from flask import Flask

import settings

from apps.auth import bp as auth_bp


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    # 注册用户登录蓝图
    app.register_blueprint(auth_bp)
    return app
