
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, UserMixin):
    """
        User class and database table

        Attributes: username, password (hashed)

        Methods: Signup (cls), Login (cls)
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
    )
    password = db.Column(
        db.String(80),
        nullable=False,
    )

    loves_cafes = db.Relationship('Cafe', secondary='users_cafes', backref='lovers')

    @classmethod
    def signup(cls, username, password):
        """
            Creates password hash and returns new user with hashed password
        """

        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        return cls(username=username, password=hashed_password)

    @classmethod
    def login(cls, username, password):
        """
            Checks if user exists in DB, then compares password hashes

            Returns an instance of the user if found and passwords match
            else False
        """

        user = cls.query.filter_by(username=username).one_or_none()
        if user and bcrypt.check_password_hash(user.password, password):
            return user

        return False

    def __repr__(self):
        return f"User: {self.username}"


class Cafe(db.Model):
    """
        Cafe class and database table

        Methods: create (cls), remove(cls)
    """

    __tablename__ = "cafes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(30),
        nullable=False,
    )

    address_street = db.Column(
        db.String(30),
        nullable=False,
    )

    address_state = db.Column(
        db.String(20),
        nullable=False
    )

    image_url = db.Column(
        db.String(50),
        default='default'
    )

    @classmethod
    def create(cls, name, address_street, address_state):
        """
            Create a new cafe and return the instance
        """
        return cls(name=name,
                   address_street=address_street,
                   address_state=address_state)

    def __repr__(self):
        return f"Cafe name:{self.name}"


class UsersCafes(db.Model):
    """
        Linking table to create many:many relationship between users:cafes
    """

    __tablename__ = "users_cafes"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafes.id'), primary_key=True)


################################################################################
# Helpers


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)
