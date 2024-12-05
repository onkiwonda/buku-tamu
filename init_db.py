import sqlite3

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('guestbook.db')

# Membuat cursor untuk mengeksekusi perintah SQL
cursor = conn.cursor()

# Membuat tabel guestbook jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS guestbook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    nama TEXT,
    tujuan TEXT,
    instansi TEXT,
    keperluan TEXT
)
''')

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()

print("Database dan tabel guestbook berhasil dibuat.")
