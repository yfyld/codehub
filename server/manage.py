# import os
# from app import create_app, db
# from app.models import User, Role  #导入数据库的两个模型
# from flask.ext.script import Manager, Shell   #导入flask_script 
# from flask.ext.migrate import Migrate, MigrateCommand  #导入flask_migrate  

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# manager = Manager(app)
# migrate = Migrate(app, db)

# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
#     manager.add_command("shell",         #避免重复导入数据库模型
#     Shell(make_context=make_shell_context))
#     manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     manager.run()

from flask_script import Manager

from app.app import user_datastore, create_app

app = create_app()

manager = Manager(app)

@manager.command
def test():
    print(u'test run')
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)