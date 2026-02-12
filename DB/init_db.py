import sqlite3

conn = sqlite3.connect('TokoSejahtera.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM riwayat_transaksi WHERE id = ?", ('1', ))
cursor.execute("DELETE FROM riwayat_transaksi WHERE id = ?", ('2', ))
conn.commit()
conn.close()
