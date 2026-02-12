from core.function import ambil_data
from core.function import tambah_barang
from core.function import hapus_barang
from core.function import edit_barang
from core.function import tampil_tabel_barang
from core.export_csv import export_csv

def inventory_manage():
    while True:
        print("=" * 55)
        print("=           INVENTORY MANAGEMENT              =")
        print("=" * 55)
        print("= 1. Lihat Data Barang                       =")
        print("= 2. Tambah Barang (Create)                  =")
        print("= 3. Edit Barang (Update)                    =")
        print("= 4. Hapus Barang (Delete)                   =")
        print("= 5. export database ke csv                  =")
        print("= 0. Kembali ke Menu Utama                   =")
        print("=" * 55)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\n" + "-" * 55)
            print(" Lihat Data Barang")
            print("-" * 55)

            list_barang = ambil_data()
            tampil_tabel_barang(list_barang)

        elif pilihan == "2":
            print("\n" + "-" * 55)
            print(" Tambah Barang Baru")
            print("-" * 55)
            barcode = input("Barcode        : ")
            name    = input("Nama Barang    : ")
            price   = input("Harga          : ")
            stok    = input("Stok           : ")
            tambah_barang(barcode, name, price, stok)


        elif pilihan == "3":
            print("\n" + "-" * 55)
            print(" Edit Data Barang")
            print("-" * 55)
            list_barang = ambil_data()
            tampil_tabel_barang(list_barang)

            print("ketik *back* jika ingin membatalkan")
            select_id = input("pilih ID barang yang ingin di edit : ")
            if select_id == "back":
                return
            barcode = input("Masukkan barcode barang: ")
            name = input("masukan nama barang : ")
            price = input("masukan harga barang : ")
            stok = input("masukan stok barang : ")
            edit_barang(select_id, barcode, name, price, stok)
        

            
        elif pilihan == "4":
            print("\n" + "-" * 55)
            print(" Hapus Data Barang")
            print("-" * 55)
            list_barang = ambil_data()
            tampil_tabel_barang(list_barang)
            print("ketik *back* jika ingin membatalkan")
            select_id = input("pilih ID barang yang ingin di hapus : ")
            confirm = input("apakah anda yakin ingin menghapus barang ini? y/n : ")
            if confirm == "y":
                hapus_barang(select_id)
            elif confirm == "back":
                return

        elif pilihan == '5':
            tabel_list = ["barang", "riwayat_transaksi", "riwayat_transaksi_Log"]

            for tabel in tabel_list:
                export_csv(tabel)

        elif pilihan == "0":
            print("\nKembali ke menu utama...")
            
            return

        else:
            print("\nPilihan tidak valid!")
