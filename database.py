import os
from dotenv import load_dotenv
load_dotenv(override=True)
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor(buffered=True)

print("Database Connected Successfully")