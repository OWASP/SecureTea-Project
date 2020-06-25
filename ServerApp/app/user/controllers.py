from sqlalchemy.exc import IntegrityError
from app import *
from .models import User

mod_user = Blueprint('user', __name__)

NET_SEC_PASSWD = 'PASSWD'
NETWORK_SECRET = NET_SEC_PASSWD

try:
    logged_in = pickle.load(open('logged_in', 'rb'))
except:
    logged_in = []

def is_logged_in(username):
    """Check if the user with given username is logged in or not

    Parameters:
        username: username of the user
    Returns:
        Boolean variable whether the username is logged in or not
    """
    return username in logged_in

@mod_user.route('/userlogin', methods=['POST'])
def login():
    """Endpoint to manage user login"""
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
    """Endpoint to manage user logout"""
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
    """Endpoint to create anew user"""
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
