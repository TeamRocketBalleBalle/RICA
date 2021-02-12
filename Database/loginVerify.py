from Database.Database_connection import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app


def login(email: str, password: str) -> bool:
    """
    This function takes the user's email, password as input and returns boolean value whether the password is correct
    or not

    # Pseudocode:
    * if email exists in database, good
      else, return None
    * if password matches with the database, good
      else, return False

    # Function names I'm assuming:
    - check_existence(email) -> bool
    - get_password(email) -> str
    """
    if check_existence(email):
        # check password now
        current_app.logger.debug(f"password: {password}\tgenerated hash:{generate_password_hash(password)}\nhash: {get_password(email)}\ncheck_password: {check_password_hash(get_password(email), password)}")
        if check_password_hash(get_password(email), password):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(check_existence('ysh@123.com'))
