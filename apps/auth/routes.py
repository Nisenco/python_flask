from apps.auth import bp

from flask import render_template, url_for

users = []


@bp.route('/')
def user():
    return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return '登录页面'


@bp.route('/logout')
def logout():
    return '退出成功'


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return '注册成功'
