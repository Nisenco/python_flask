from flask_script import Manager

from apps import creat_app

app = creat_app()
manager = Manager(app)
if __name__ == '__main__':
    manager.run()
