from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            database=os.getenv("POSTGRES_DB", "flaskapp"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host=os.getenv("POSTGRES_HOST", "postgres"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        return conn, None  
    except Exception as e:
        return None, str(e)  


@app.route("/")
def index():
    conn, error = connect_db()
    if conn:
        conn.close()  
        return "Connected to PostgreSQL!"
    else:
        return f"Database connection failed: {error}", 500  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
