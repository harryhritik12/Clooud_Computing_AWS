import mysql.connector


def create_database_and_table(host_name, user_name, user_password, db_name):
    # Create a connection
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password
    )

    cursor = connection.cursor()

    # Create a new database (if it doesn't exist)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    # Switch to the new database
    cursor.execute(f"USE {db_name}")

    # Create a feedback table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Feedback (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Message TEXT NOT NULL
    )
    """)

    cursor.close()
    connection.close()


def insert_feedback(host_name, user_name, user_password, db_name, message):
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=db_name
    )

    cursor = connection.cursor()

    cursor.execute("INSERT INTO Feedback (Message) VALUES (%s)", (message,))
    connection.commit()

    cursor.close()
    connection.close()


def retrieve_feedback(host_name, user_name, user_password, db_name):
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=db_name
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Feedback")
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


# Configuration and Usage
RDS_HOSTNAME = "rdsinstance.cfphmmyx15za.ap-south-1.rds.amazonaws.com"  # Make sure to replace with your RDS endpoint.
DB_USERNAME = "admins"
DB_PASSWORD = "12345678"
DATABASE_NAME = "FeedbackDB"

# Call the functions as per your requirements. Here's an example:
create_database_and_table(RDS_HOSTNAME, DB_USERNAME, DB_PASSWORD, DATABASE_NAME)
insert_feedback(RDS_HOSTNAME, DB_USERNAME, DB_PASSWORD, DATABASE_NAME, "This is a test feedback.")
feedbacks = retrieve_feedback(RDS_HOSTNAME, DB_USERNAME, DB_PASSWORD, DATABASE_NAME)

for feedback in feedbacks:
    print(feedback)