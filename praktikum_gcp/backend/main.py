from flask import Flask, request, jsonify
import os
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME")
    )

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kegiatan (nama, nim, email) VALUES (%s, %s, %s)", 
                       (data["nama"], data["nim"], data["email"]))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/kegiatan')
def get_kegiatan():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT nama, nim, email, waktu FROM kegiatan ORDER BY waktu DESC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
