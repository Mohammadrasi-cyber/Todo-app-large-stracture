import os
from app import create_app, db
from app.users.models import User
from app.todos.models import Todo
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
   return dict(db=db, User=User, Todo=Todo)
