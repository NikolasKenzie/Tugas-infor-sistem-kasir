#page
from view.kasir import kasirPage
from view.inventoryManage import inventory_manage
from view.riwayatTransaksi import tabel_riwayat_transaksi
from view.riwayatTransaksi import tabel_riwayat_transaksiLog

def mainApp():
    while True:
        print("=" * 45)
        print("=         SELAMAT DATANG DI TOKO SEJAHTERA         =")
        print("=" * 45)
        print("=                 MENU UTAMA                      =")
        print("=" * 45)
        print("= 1. Kasir                                        =")
        print("= 2. Inventory Management                         =")
        print("= 3. Riwayat Transaksi                            =")
        print("= 0. Tutup applikasi                              =")
        print("=" * 45)

        page_select = input("Silahkan pilih halaman: ")

        if page_select == "1":
            kasirPage()
        elif page_select == "2":
            inventory_manage()
        elif page_select == "3":
            tabel_riwayat_transaksi()
        elif page_select == "0":
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    mainApp()
    




