import imaplib, json, pdb, sys, os, psycopg2
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = os.path.abspath(CURRENT_DIR)
PARENT_DIR = os.path.join(CURRENT_DIR, '..')
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from dotenv import load_dotenv

load_dotenv()  # take the environment variables from .env file.

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_SSL_MODE = os.getenv('DB_SSL_MODE')


def execute_query(query: str) -> list:
    results: list = []
    try: 
        conn = psycopg2.connect(
            host = DB_HOST,
            port = DB_PORT,
            database = DB_NAME,
            user = DB_USERNAME,
            password = DB_PASSWORD
        )

        cur = conn.cursor()
        cur.execute(query)
        results: list = cur.fetchall()
        cur.close()
        conn.close()        
    except RuntimeError as error:
        raise error
    return results
