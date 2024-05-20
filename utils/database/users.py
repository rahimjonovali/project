import psycopg2


def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="group1",
        user="postgres",
        password="7",
        port="5432"
    )
    conn.autocommit = True
    return conn


def close_db_connection(conn):
    if conn:
        conn.close()


def create_user(fio, username, chat_id):
    conn = connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        insert into users (fio, username,chat_id) values ('{fio}','{username}','{chat_id}')
        """)

    close_db_connection(conn)


def update_user(phone, chat_id):
    conn = connect_to_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""UPDATE users SET phone = '{phone}' WHERE chat_id = '{chat_id}';""")
    close_db_connection(conn)


def delete_user(chat_id):
    conn = connect_to_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""
            DELETE FROM users
            WHERE chat_id = {chat_id};
        """)
    close_db_connection(conn)


def get_user_by_id(chat_id):
    conn = connect_to_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM users
            WHERE chat_id = '{chat_id}';
        """)
        result = cursor.fetchone()
    close_db_connection(conn)
    return result


def get_user():
    conn = connect_to_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM users;
        """)
        result = cursor.fetchall()
    close_db_connection(conn)
    return result
