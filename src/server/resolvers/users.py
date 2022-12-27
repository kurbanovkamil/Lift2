from server.sql_base.archeology_db import base_worker
from server.sql_base.models import User

def check_login(user: User) -> int:
    query = "SELECT post FROM users WHERE login = ? AND password = ?"
    return base_worker.execute(query, args = (user.login, user.password))