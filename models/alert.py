import psycopg2
from datetime import date

DB_CONFIG = {
    "host": "your-postgres-service",  # In K3s this will be your Postgres service name
    "port": 5432,                     # Use your internal Postgres port
    "dbname": "postgres",
    "user": "postgres",
    "password": "Password1!"
}

def check_alerts():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    sql = """
    SELECT warning_id, event_code, event_en, warning_level, event_description, approximate_start
    FROM smhi.weather_warnings
    WHERE warning_level IN ('Yellow', 'Orange', 'Red')
    AND area_name ILIKE '%stockholm%'
    AND approximate_start::date = %s
    ORDER BY approximate_start;
    """

    cur.execute(sql, (date.today(),))
    rows = cur.fetchall()

    if rows:
        print("🚨 ALERT: Warnings for Stockholm today:")
        for row in rows:
            print(f"ID: {row[0]} | {row[1]} - {row[2]} | Level: {row[3]} | Desc: {row[4]} | Start: {row[5]}")
        # Here you could call a Slack webhook or email API
    else:
        print("✅ No active warnings for Stockholm today.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    check_alerts()
