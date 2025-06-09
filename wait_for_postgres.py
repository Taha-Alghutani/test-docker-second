# wait_for_postgres.py
import time
import psycopg2
from psycopg2 import OperationalError
import os

DB_NAME = os.environ.get("POSTGRES_DB", "django_db")
DB_USER = os.environ.get("POSTGRES_USER", "root")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "example")
DB_HOST = os.environ.get("DB_HOST", "postgres")
DB_PORT = os.environ.get("DB_PORT", 5432)

while True:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        print("✅ PostgreSQL is ready!")
        conn.close()
        break
    except OperationalError:
        print("⏳ Waiting for PostgreSQL to be ready...")
        time.sleep(1)
