from flask import Flask, request, jsonify, render_template
# new
app = Flask(__name__)

# Database credentials
RDS_HOSTNAME = "rdsinstanceminshu.cj8uuw5ykjac.ap-south-1.rds.amazonaws.com"
DB_USERNAME = "admins"
DB_PASSWORD = "12345678"
DATABASE_NAME = "FeedbackDB"

import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host=RDS_HOSTNAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DATABASE_NAME
    )
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        name = request.form['name']
        message = request.form['message']
        insert_query = "INSERT INTO feedback (Name, Message) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, message))
        connection.commit()
        return jsonify({"status": "success", "message": "Feedback submitted successfully!"})
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)})
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
