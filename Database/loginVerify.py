from Database.Database_connection import *


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
        if password == get_password(email):
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    print(check_existence('ysh@123.com'))
