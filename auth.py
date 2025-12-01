import hashlib
from db import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username,password,role):
    role = role.upper()
    hashed_pw = hash_password(password)
    sql = '''insert into USERS(USER_NAME,HASHED_PASSWORD,ROLE) values(%s,%s,%s)'''
    conn = get_connection()
    curs = conn.cursor()
    try:
        curs.execute(sql,(username,hashed_pw,role))
        conn.commit()
        return True
    except Exception as e:
        print(f'Error inserting user: {e}')
        conn.rollback()
        return False

    finally:
        conn.close()

def login_user(username,password):
    hashed_pw = hash_password(password)
    sql1 = 'select ROLE from USERS where USER_NAME = %s AND HASHED_PASSWORD = %s'
    conn = get_connection()
    curs = conn.cursor()
    curs.execute(sql1,(username, hashed_pw))

    result = curs.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None