from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    This is a class for building user model
      
    Attributes:
        id (int): Id of the user (autoincremental)
        username (string): Username for a user
        password (string): Hashed password of a user
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        """Initialize a user model

        Parameters:
            username(string): Username of the user
            password(string): Password of the user
        """
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Checking password using hash

        Parameters:
            password: Password to be checked as a string
        Returns:
            Boolean variable whether the password is correct or not
        """
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Convert user data to dictionary
            Returns:
                A dictionary of the data of the user
        """
        return {
            'id' : self.id,
            'username': self.username,
        }

    def __repr__(self):
        """Representing a user model
            Returns:
                A string of the representation of the user
        """
        return "User<%d> %s" % (self.id, self.username)
