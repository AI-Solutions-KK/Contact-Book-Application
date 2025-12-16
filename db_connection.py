"""Database connection module"""
import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Get Oracle database connection"""
    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        service_name=os.getenv("DB_SERVICE")
    )

def insert_contact(full_name, phone_number):
    """Insert contact into database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO contacts (full_name, phone_number) VALUES (:1, :2)"
    cursor.execute(sql, (full_name, phone_number))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True

def search_contacts(search_term=""):
    """Search contacts by name"""
    conn = get_connection()
    cursor = conn.cursor()
    
    if search_term:
        sql = "SELECT id, full_name, phone_number, created_date FROM contacts WHERE UPPER(full_name) LIKE UPPER(:1) ORDER BY full_name"
        cursor.execute(sql, (f"%{search_term}%",))
    else:
        sql = "SELECT id, full_name, phone_number, created_date FROM contacts ORDER BY full_name"
        cursor.execute(sql)
    
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return results