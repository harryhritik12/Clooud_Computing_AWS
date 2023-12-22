from flask import Flask, request, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

# Database credentials with intentional error
RDS_HOSTNAME = "rdsinstanceminshu.cj8uuw5ykjac.ap-south-1.rds.amazonaws.com"
DB_USERNAME = "admins"
DB_PASSWORD = "12345678"
DATABASE_NAME = "FeedbackDB"

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
    with open('index.html', 'r') as f:
        content = f.read()
        return render_template_string(content)

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        name = request.form['name']
        message = request.form['message']
        insert_query = "INSERT INTO feedback(name, message) VALUES (%s, %s)"
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