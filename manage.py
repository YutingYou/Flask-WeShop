# -*- coding: utf-8 -*-
import os
from weshop import create_app
from flask_script import Manager, Shell
from weshop.extensions import db
from weshop.shop.models import User
from weshop.constants import Role
from configs.config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

# 目的是省去import app db User等对象，一次性导入
def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def db_reset():
    db.drop_all()
    print('db.drop_all()')

    db.create_all()
    print('db.create_all()')

    from sqlalchemy.exc import IntegrityError
    u = User(role=Role.ADMIN,
             username=Config.ADMIN_USERNAME,
             openid=Config.ADMIN_OPENID)
    db.session.add(u)

    try:
        db.session.commit()
    except IntegrityError:
        print('ERROR, add admin account.')
        db.session.rollback()

if __name__ == '__main__':
    manager.run()






