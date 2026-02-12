from datetime import datetime
today_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

from core.idTransaksiGenerator import generate_id_transaksi
from core.function import pilih_barang
from core.function import edit_barang
from core.function import perbarui_stok
from core.function import simpan_riwayat_transaksi
from core.function import simpan_riwayat_transaksi_log

def kasirPage():
    print("=" * 55)
    print("=                   KASIR                    =")
    print("=" * 55)
    print("Ketik b untuk kembali ke menu")
    print("Ketik f untuk melanjutkan pembayaran\n")

    list_belanja = []

    while True:
        input_barang = input("Masukkan barcode / nama barang : ")

        if input_barang == "b":
            print("\nKembali ke menu utama...")
            break

        if input_barang == "f":
            diskon_input = input("Masukan diskon : ")
            diskon = float(diskon_input)

            if len(list_belanja) == 0:
                print("Keranjang masih kosong!\n")
                continue

            print("\n========== STRUK BELANJA ==========")
            print("\n========== TOKOSEJAHTERA ==========")
            total_kotor = 0
            for item in list_belanja:
                subtotal = item["price"] * item["qty"]
                total_kotor += subtotal
                print(f'{item["name"]} x{item["qty"]} = Rp {subtotal}')

            potongan_diskon = total_kotor * (diskon / 100)
            total_setelah_diskon = total_kotor - potongan_diskon
            ppn = total_setelah_diskon * 0.11
            total_akhir = total_setelah_diskon + ppn
            print("----------------------------------")
            print(f"Total Barang  : Rp {total_kotor}")
            if potongan_diskon > 0:
                print(f"Diskon ({diskon}%) : -Rp {potongan_diskon}")

            print(f"PPN (11%)     : +Rp {ppn}")
            print(f"TOTAL AKHIR   : Rp {total_akhir}")
            print("==================================")
            konfirmasi = input("Lanjut pembayaran? (y/n): ")
            nama_transaksi = input("Masukan Nama Transaksi: ")

            if konfirmasi.lower() == "y":
                while True:
                    uang_pembeli = int(input('masukan uang pembeli : '))
                    if uang_pembeli < total_akhir:
                        print("Uang pembeli tidak cukup!")
                        continue
                    uang_kembali = uang_pembeli - total_akhir
                    break
                print(f"kembalian : {uang_kembali}")
                print("\nPembayaran berhasil. Terima kasih!\n")
                
                id_transaksi = generate_id_transaksi()
                simpan_riwayat_transaksi(id_transaksi, nama_transaksi, today_date, total_akhir)
                for item in list_belanja:
                    simpan_riwayat_transaksi_log(id_transaksi, item['name'], item['price'], item['qty'])

                for item in list_belanja:
                    perbarui_stok(item['id'], item['qty'])
                list_belanja.clear()
                continue
            else:
                print("\nKembali ke input barang...\n")

            continue

        result = pilih_barang(input_barang)

        if result == None:
            print("Barang tidak ditemukan!\n")
            continue

        input_jumlah = input("Masukkan jumlah barang        : ")

        barang = {
            "id": result["id"],
            "barcode": result["barcode"],
            "name": result["name"],
            "price": result["price"],
            "qty": int(input_jumlah)
        }

        list_belanja.append(barang)
        print("Barang berhasil ditambahkan ke keranjang\n")
