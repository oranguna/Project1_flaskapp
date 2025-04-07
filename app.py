from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Set up PostgreSQL connection info (adjust these values to match your setup)
DB_HOST = "localhost"  # PostgreSQL server address
DB_NAME = "your_database_name"  # Your PostgreSQL database name
DB_USER = "your_user_name"  # Your PostgreSQL username
DB_PASSWORD = "your_password"  # Your PostgreSQL password

# Initialize the database path for SQL initialization script
INIT_PATH = os.path.join(os.path.dirname(__file__), "init_db.sql")


def init_db():
    """Initialize the database if it doesn't exist by running the init_db.sql script."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
        cursor = conn.cursor()

        # Execute the init_db.sql script to set up the tables
        with open(INIT_PATH, "r") as f:
            cursor.execute(f.read())

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error initializing the database:", e)


def get_messages():
    """Retrieve all messages from the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        print("Error fetching messages:", e)
        return []


@app.route("/")
def home():
    """Render the homepage with the messages."""
    messages = get_messages()
    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    init_db()  # Initialize the database before running the app
    app.run(host="0.0.0.0", port=5000)

