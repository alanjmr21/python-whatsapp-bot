import psycopg2
import os

def create_connection():
  # Get the DATABASE_URL from environment variables
  database_url = os.environ.get("POSTGRESQL_DATABASE_URI")
  # Establish a connection
  conn = psycopg2.connect(database_url)
  # Create a cursor
  cursor = conn.cursor()

  return cursor, conn