from flask import Flask, render_template
import settings
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='db',
                            database='scrapyDB',
                            user="docker",
                            password="docker")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM data;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)


app.run(debug=True, host='0.0.0.0', port=8080)