import sqlite3
import random
from core.database import connect_to_database

def tampil_tabel_barang(data):
    print("=" * 78)
    print("| No | ID | Barcode | Nama Barang |   Harga   | Stok |")
    print("=" * 78)
    list_barang = [dict(row) for row in data]

    for i, item in enumerate(list_barang, start=1):
        print(
            f"| {i:<2} "
            f"| {item['id']:<2} "
            f"| {item['barcode']:<7} "
            f"| {item['name']:<11} "
            f"| Rp {item['price']:<7} "
            f"| {item['stok']:<4} |"
        )

    print("=" * 78)


def ambil_data():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang")
    row = cursor.fetchall()
    return row
    conn.commit()
    conn.close()


def pilih_barang(data):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang WHERE barcode LIKE ? OR name LIKE ?", (data, data))
    results = cursor.fetchone() 
    return results
    conn.commit()
    conn.close()
    

def tambah_barang(barcode, name, price, stok):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO barang (barcode, name, price, stok) VALUES (?, ?, ?, ?)", 
            (barcode, name, price, stok)
        )
        conn.commit()
        print(f"Barang '{name}' berhasil ditambah!")

    except sqlite3.IntegrityError:
        print(f"Gagal: Barcode '{barcode}' sudah terdaftar di sistem.")
    
    except Exception as e:
        print(f"Terjadi kesalahan sistem: {e}")

    finally:
        conn.close()
    

def edit_barang(id, barcode, name, price, stok):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE barang SET barcode = ?, name = ?, price = ?, stok = ? WHERE id = ?",
        (barcode, name, price, stok, id)
    )
    conn.commit()
    conn.close()
    print(f"{name} berhasil ditambahkan")

def hapus_barang(id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM barang WHERE id = ?",
        (id, )
    )
    conn.commit()
    conn.close()

def perbarui_stok(id, jumlah_pengurangan):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT stok FROM barang WHERE id = ?", (id,)
    )
    stok_barang = cursor.fetchone()
    stok_sekarang = stok_barang["stok"]
    stok_update = stok_sekarang - int(jumlah_pengurangan)
    cursor.execute(
        "UPDATE barang SET stok = ? WHERE id = ?", (stok_update, id)
    )
    conn.commit()
    conn.close()
    
#id transaksi = random number

def simpan_riwayat_transaksi(id_transaksi, nama_transaksi, tanggal, total):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO riwayat_transaksi (id_transaksi, nama_transaksi, tanggal, total) VALUES(?, ?, ?, ?)",
        (id_transaksi, nama_transaksi, tanggal, total)
    )
    conn.commit()
    conn.close()

def simpan_riwayat_transaksi_log(id_transaksi, barang,  price, jumlah):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO riwayat_transaksi_log (id_transaksi, barang, price, jumlah) VALUES (?, ?, ?, ?)",
        (id_transaksi, barang, price, jumlah)
    )

    conn.commit()
    conn.close()
def lihat_riwayat_transaksi():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM riwayat_transaksi"
    )
    data = cursor.fetchall()
    return data
    conn.commit()
    conn.close()
    
def lihat_riwayat_transaksiLog(id_transaksi):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM riwayat_transaksi_log WHERE id_transaksi = ?",
        (id_transaksi, )
    )
    data = cursor.fetchall()
    return data
    conn.commit()
    conn.close()

