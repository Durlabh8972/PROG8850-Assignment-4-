import mysql.connector

def test_subscriber_table():
    conn = mysql.connector.connect(host="localhost", user="root", password="durlabh123", database="subscribers")
    cursor = conn.cursor()
    cursor.execute("DESCRIBE subscribers;")
    columns = [column[0] for column in cursor.fetchall()]
    assert "email" in columns, "Missing 'email' column"
    assert "subscription_date" in columns, "Missing 'subscription_date' column"
    print("Schema validation passed.")
    conn.close()

if __name__ == "__main__":
    test_subscriber_table()
