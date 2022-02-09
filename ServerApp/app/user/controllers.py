from sqlalchemy.exc import IntegrityError
from app import *
from .models import User
import sqlite3

mod_user = Blueprint('user', __name__)

NET_SEC_PASSWD = 'PASSWD'
NETWORK_SECRET = NET_SEC_PASSWD
net_sec = NET_SEC_PASSWD

def is_logged_in(username):
    """Check if the user with given username is logged in or not

    Parameters:
        username: username of the user
    Returns:
        Boolean variable whether the username is logged in or not
    """
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM users ORDER BY username'):
        print(row)
    
    for c1 in cur.execute("SELECT EXISTS(SELECT * FROM users WHERE username='" + username + "')"):
        print("isloggedin username password is correct")
        return True




@mod_user.route('/userlogin', methods=['POST'])
def login():
    """Endpoint to manage user login"""
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    # Insert a row of data
    uname = request.json["username"]
    passwd = request.json["password"]
    ns = request.json["ns"]
    try:
        if ns == net_sec :
            temp = 0
            for c1 in cur.execute("SELECT EXISTS(SELECT * FROM users WHERE username='" + uname + "' AND password='" + passwd + "')"):
                print("username password is correct")
                return jsonify('logged in')
            else:
                print("username password incorrect")
                return jsonify('username password incorrect')
        else:
            print("Network Secret is incorrect")
    except sqlite3.IntegrityError:
        print('Something went wrong')
        return jsonify('Something went wrong')


    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    for row in cur.execute('SELECT * FROM users ORDER BY username'):
            print(row)

    con.close()
    return jsonify('Login Sucessful')




    try:
        username = request.json['username']
        password = request.json['password']
        ns = request.json['ns']
        print("\n" + username + "\n" + password + "\n" + ns + "\n")
        if ns != NETWORK_SECRET:
            return 'Wrong secret', 402
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    user = User.query.filter(User.username == username).first()
    if user is None or not user.check_password(password):
        return "401", 401
    print(username + "\nCreds are correct")
    """
    try:
        session['logged_in'].append(username)
    except:
        session['logged_in'] = [username]
    logged_in.append(username)
    pickle.dump(logged_in, open('logged_in', 'wb'))
    session['logged_in'] = logged_in
    """
    return "200", 200

@mod_user.route('/userlogout', methods=['POST'])
def logout():
    """Endpoint to manage user logout"""
    """
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
    """
    return jsonify(success=True)

@mod_user.route('/register', methods=['POST'])
def create_user():
    """Endpoint to create anew user"""


    con = sqlite3.connect('example.db')
    cur = con.cursor()

    try:
        # Create table
        cur.execute('''CREATE TABLE users(username text NOT NULL PRIMARY KEY, password text)''')
    except sqlite3.OperationalError:
        print("Users table exists. Skipping creation")
    
    # Insert a row of data
    uname = request.json["username"]
    passwd = request.json["password"]
    ns = request.json["ns"]
    try:
        if ns == net_sec :
            sql_query = "INSERT INTO users VALUES ('" + uname + "','" + passwd + "')"
            cur.execute(sql_query)
        else:
            print("Network Secret is incorrect")
    except sqlite3.IntegrityError:
        print('Two users with same Username')
        return jsonify('Two users with same Username')


    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    for row in cur.execute('SELECT * FROM users ORDER BY username'):
            print(row)

    con.close()
    return jsonify('Registration Sucessful'), 200


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