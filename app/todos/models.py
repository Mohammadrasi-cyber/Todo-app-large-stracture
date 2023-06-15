from app import db
from datetime import datetime
from app.users.models import User

class  Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(32),unique=False)
    note = db.Column(db.Text(),unique=True)
    done =  db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    def __repr__(self):
        return self.title  
    
    def from_json_update(self,todo_json):
        title = todo_json.get('title',self.title)
        done = todo_json.get('done',self.done)
        note = todo_json.get('note',self.note)
        self.title = title
        self.done = done
        self.note = note
        db.session.add(self)
        db.session.commit()
        return self
    
    def get_author(self,author_id):
        
        user=User.query.filter_by(id=author_id).first()
        data={'email':user.email}
        return data
    
    def to_json(self):
        json_post = {
        'id':self.id,
        'note': self.note,
        'title':self.title,
        'done':self.done,
        'created_at': self.created_at,
        'author':self.get_author(self.author)
        }
        return json_post 