from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', 'rootpassword'),
    'database': os.environ.get('MYSQL_DATABASE', 'grampanchayat')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        aadhar = request.form['aadhar']
        panipatti = request.form['panipatti']
        date = request.form['date']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO forms (name, mobile, aadhar, panipatti, date) VALUES (%s, %s, %s, %s, %s)",
                       (name, mobile, aadhar, panipatti, date))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

    return render_template('index.html')

@app.route('/admin')
def admin():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM forms")
    forms = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('admin.html', forms=forms)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
