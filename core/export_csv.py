import sqlite3
import csv
import os

def export_csv(nama_tabel):
    conn = None 
    try:
        
        db_path = os.path.join(os.path.dirname(__file__), "..", "DB", "TokoSejahtera.db")
        
        
        if not os.path.exists(db_path):
            print(f"Error: Database tidak ditemukan di {db_path}")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        
        cursor.execute(f"SELECT * FROM {nama_tabel}")
        rows = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]
        
        file_name = f"{nama_tabel}_export.csv"
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(column_names)
            writer.writerows(rows)

        print(f"Berhasil! File {file_name} telah dibuat.")
        print(f"Lokasi: {os.path.abspath(file_name)}")

    except Exception as e:
        print(f"Gagal export {nama_tabel}: {e}")
    finally:
        
        if conn:
            conn.close()

