import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()  # load .env variables

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """
    Returns a new connection to the Supabase Postgres database.
    """
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def extract_raw_data_from_db():
    """
    Fetch all rows from the databaseBot table as a single string,
    similar to how your SQLite version worked.
    """
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM public."databaseBot"')
    rows = cur.fetchall()
    conn.close()

    # Convert rows to string (NULLs become empty strings)
    db_content = "\n".join([
        " ".join([str(v) if v is not None else "" for v in row.values()])
        for row in rows
    ])
    return db_content