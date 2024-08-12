import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        user= ('DB_USER'),
        password= ('DB_PASSWORD'),
        host= ('DB_HOST'),
        port= ('DB_PORT'),
        database= ('DB_NAME')
    )
    return conn
