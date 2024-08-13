"""Init file for DB Stuff."""
import psycopg2
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_table_data():
    # Database connection parameters
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_NAME = os.getenv("POSTGRES_NAME")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_PORT = os.getenv("POSTGRES_PORT")

    try:
        print("Fetching table data", flush=True)
        
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

        cursor = connection.cursor()

        # SQL query to fetch data from a table
        cursor.execute("SELECT * FROM source_url;")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names from the cursor
        col_names = [desc[0] for desc in cursor.description]

        # Convert rows to list of dictionaries
        result = [dict(zip(col_names, row)) for row in rows]

        # Convert the result to a JSON object
        result_json = json.dumps(result, indent=4)

        return result_json

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None
    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")