import mysql.connector

# Your MySQL server details
HOST = "rdsinstance.cfphmmyx15za.ap-south-1.rds.amazonaws.com"
USER = "admins"
PASSWORD = "12345678"
DATABASE = "FeedbackDB"






connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
cursor = connection.cursor()

# Create personal_details table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS personal_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    dob DATE,
    gender VARCHAR(10),
    age INT,
    school_name VARCHAR(255),
    college_name VARCHAR(255)
)
""")

# Create feedback table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    message TEXT
)
""")