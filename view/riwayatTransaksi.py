from core.function import lihat_riwayat_transaksi
from core.function import lihat_riwayat_transaksiLog

def tabel_riwayat_transaksi():
    while True:
        data_riwayat = lihat_riwayat_transaksi()
        list_data = [dict(row) for row in data_riwayat]

        print("\n" + "=" * 90)
        print("| No | ID Transaksi | Nama Transaksi |   Tanggal   |   Total   |")
        print("=" * 90)

        for i, item in enumerate(list_data, start=1):
            print(
                f"| {i:<2} "
                f"| {item['id_transaksi']:<12} "
                f"| {item['nama_transaksi']:<15} "
                f"| {item['tanggal']:<11} "
                f"| Rp {item['total']:<8} |"
            )

        print("=" * 90)
        print("Ketik Id transaksi untuk lihat detail")
        print("Ketik 0 untuk kembali ke menu utama")

        pilih_id = input("Pilihan: ")

        if pilih_id == "0":
            return  
        tabel_riwayat_transaksiLog(pilih_id)


def tabel_riwayat_transaksiLog(id_transaksi):
    while True:
        data_log = lihat_riwayat_transaksiLog(id_transaksi)
        list_log = [dict(row) for row in data_log]

        print("\n" + "=" * 90)
        print(f"DETAIL TRANSAKSI ID: {id_transaksi}")
        print("=" * 90)
        print("| No | Barang         | Harga       | Jumlah    |")
        print("=" * 90)

        for i, item in enumerate(list_log, start=1):
            print(
                f"| {i:<2} "
                f"| {item['barang']:<15} "
                f"| Rp {item['price']:<6} "
                f"| {item['jumlah']:<6} |"
            )

        print("=" * 90)
        print("Tekan ENTER untuk kembali ke riwayat transaksi")

        back = input()
        if back == "":
            return  
