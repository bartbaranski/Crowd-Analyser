import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

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

def add_analysis_result(event_id, participant_count, crowd_density, avg_people_per_minute):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = sql.SQL("""
        INSERT INTO Analyses (event_id, participant_count, crowd_density, average_participants_per_minute)
        VALUES (%s, %s, %s, %s);
    """)
    
    cursor.execute(query, (event_id, participant_count, crowd_density, avg_people_per_minute))
    conn.commit()
    cursor.close()
    conn.close()


