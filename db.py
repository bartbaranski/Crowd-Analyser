import psycopg2
from psycopg2 import sql

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/crowd_analysis"

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def add_video(file_path, format):
    conn = get_connection()
    cursor = conn.cursor()
    query = sql.SQL("""
                    INSERT INTO Videos (file_path, format) VALUES (%s, %s) RETURNING id;""")
    cursor.execute(query, (file_path, format))
    video_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return video_id
