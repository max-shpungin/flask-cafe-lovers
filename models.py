

class User():
    """
        User class and database table

        Attributes: username, password (hashed)

        Methods: Signup (cls), Login (cls)
    """
    username = ''
    password = ''
    ...

    @classmethod
    def signup(cls, username, password):
        """
            Creates password hash and returns new user with hashed password

            Raises IntegrityError if username already exists
        """

    @classmethod
    def login(cls, username, password):
        """
            Checks if user exists in DB, then compares password hashes

            Returns an instance of the user if found, else False
        """

class Cafe():
    """
        Cafe class and database table

        Methods: create (cls), remove(cls)
    """
    ...

class UsersCafes():
    """
        Linking table to create many:many relationship between users:cafes
    """