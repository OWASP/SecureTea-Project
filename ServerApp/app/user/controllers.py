from flask import *
from sqlalchemy.exc import IntegrityError
from app import *
from .models import User
import json

mod_user = Blueprint('user', __name__)

NETWORK_SECRET = 'PASSWD'

try:
    logged_in = pickle.load(open('logged_in', 'rb'))
except:
    logged_in = []

def is_logged_in(username):
    return username in logged_in

@mod_user.route('/userlogin', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']
        ns = request.json['ns']
        if ns != NETWORK_SECRET:
            return 'Wrong secret', 402
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    user = User.query.filter(User.username == username).first()
    if user is None or not user.check_password(password):
        return "401", 401
    try:
        session['logged_in'].append(username)
    except:
        session['logged_in'] = [username]
    logged_in.append(username)
    pickle.dump(logged_in, open('logged_in', 'wb'))
    session['logged_in'] = logged_in
    return "200", 200

@mod_user.route('/userlogout', methods=['POST'])
def logout():
    try:
        username = request.json['username']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    try:
        while(True):
            logged_in.remove(username)
    except:
        pass
    pickle.dump(logged_in, open('logged_in', 'wb'))
    return jsonify(success=True)

@mod_user.route('/register', methods=['POST'])
def create_user():
    try:
        username = request.json['username']
        password = request.json['password']
        ns = request.json['ns']
        if ns != NETWORK_SECRET:
            return 'Wrong secret', 402
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    u = User(username, password)
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(success=False, message="This username already exists"), 400

    return jsonify(success=True)
