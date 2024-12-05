from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Fungsi untuk mendapatkan koneksi ke database SQLite
def get_db_connection():
    conn = sqlite3.connect('guestbook.db')
    conn.row_factory = sqlite3.Row  # Menghasilkan dictionary seperti objek
    return conn

# Menampilkan data tamu
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM guestbook')
    guestbook_data = cursor.fetchall()
    conn.close()
    return render_template('index.html', guestbook_data=guestbook_data)

# Menambahkan data tamu
@app.route('/', methods=['POST'])
def add_guest():
    tanggal = request.form['tanggal']
    nama = request.form['nama']
    tujuan = request.form['tujuan']
    instansi = request.form['instansi']
    keperluan = request.form['keperluan']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO guestbook (tanggal, nama, tujuan, instansi, keperluan)
        VALUES (?, ?, ?, ?, ?)
    ''', (tanggal, nama, tujuan, instansi, keperluan))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
