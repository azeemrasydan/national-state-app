from fastapi import HTTPException
import mysql.connector

DATABASE_CONFIG = {
    "user": "",
    "password": "",
    "host": "",
    "database": "",
}

def execute_query(query, data=None):
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor(dictionary=True)
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")
    finally:
        cursor.close()
        connection.close()