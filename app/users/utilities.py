from .models import UserToken,User
from app import db

def check_user_token(userid):
    token = UserToken.query.filter_by(user=userid).first()
    if token:
        return token.token
    new_token = UserToken(user=userid)
    db.session.add(new_token)
    db.session.commit()
    return new_token.token


def json_login(json_login_data):
    
    password = json_login_data.get('password')
    email = json_login_data.get('email')
    if not password and not email:
        return {'message':'send password and email'}
    user=User.query.filter_by(email=email).first()
    if user is None:
        return {'message':'User Not Found'}
    elif user:
        result=user.check_password(password)
        if result:
            token=check_user_token(user.id)
            return {"message": "Login was success",'token':token}
        else:
            return {'message':'Email,Password is Wrong'}

def get_user_by_token(token):
    user = UserToken.query.filter_by(token=token).first()
    if user:
        return User.query.filter_by(id=user.id).first()
    return None

def required_login(req):
    try:            
        tk = req.authorization.token
    except:
        return {'messeage':'you have to login'},False
    else:
        return tk,True
    
def is_author_object(requsted_user,object_author):
    try:
        user=requsted_user.id
    except:
        
        return False,{'messeage':'Must be own todo'}
    
    if user == object_author:
        return True,{}
    else:
        return False,{'messeage':'Must be own todo'}
        