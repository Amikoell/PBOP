class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

class Produk:
    def __init__(self, kode_produk, nama_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

    def get_info(self):
        return f"{self.nama_produk} (Kode: {self.kode_produk}) - Harga: Rp{self.harga:,}"

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        Produk.__init__(self, kode_produk, nama_produk, harga)

    def get_info(self):
        return f"Snack: {self.nama_produk} (Kode: {self.kode_produk}) - Harga: Rp{self.harga:,}"

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        Produk.__init__(self, kode_produk, nama_produk, harga)

    def get_info(self):
        return f"Makanan: {self.nama_produk} (Kode: {self.kode_produk}) - Harga: Rp{self.harga:,}"

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        Produk.__init__(self, kode_produk, nama_produk, harga)

    def get_info(self):
        return f"Minuman: {self.nama_produk} (Kode: {self.kode_produk}) - Harga: Rp{self.harga:,}"

class Struk:
    def __init__(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

    def print_struk(self):
        return (f"=========== Struk Pembelian ===========\n"
                f"No Transaksi : {self.no_transaksi}\n"
                f"Nama Pegawai : {self.nama_pegawai}\n"
                f"Nama Produk  : {self.nama_produk}\n"
                f"Jumlah Produk: {self.jumlah_produk}\n"
                f"Total Harga  : Rp{self.total_harga:,}\n"
                f"=======================================\n")

produk_list = [
    Snack("S001", "Chips", 5000),
    Makanan("M001", "Nasi Goreng", 20000),
    Minuman("D001", "Toriyu", 7000)
]

def create_produk():
    print("\n--- Tambah Produk Baru ---")
    kode = input("Masukkan kode produk: ")
    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    kategori = input("Masukkan kategori produk (Snack/Makanan/Minuman): ").lower()
    
    if kategori == "snack":
        produk_list.append(Snack(kode, nama, harga))
    elif kategori == "makanan":
        produk_list.append(Makanan(kode, nama, harga))
    elif kategori == "minuman":
        produk_list.append(Minuman(kode, nama, harga))
    else:
        print("Kategori tidak valid.")
    print("Produk berhasil ditambahkan!\n")

def read_produk():
    print("\n=========== Daftar Produk ===========")
    for produk in produk_list:
        print(produk.get_info())
    print("=====================================\n")

def update_produk():
    kode = input("Masukkan kode produk yang akan diubah: ")
    for produk in produk_list:
        if produk.kode_produk == kode:
            nama_baru = input("Masukkan nama baru produk: ")
            harga_baru = int(input("Masukkan harga baru produk: "))
            produk.nama_produk = nama_baru
            produk.harga = harga_baru
            print("Produk berhasil diupdate!\n")
            return
    print("Produk tidak ditemukan.\n")

def delete_produk():
    kode = input("Masukkan kode produk yang akan dihapus: ")
    for produk in produk_list:
        if produk.kode_produk == kode:
            produk_list.remove(produk)
            print("Produk berhasil dihapus!\n")
            return
    print("Produk tidak ditemukan.\n")

def tampilkan_menu():
    print("\n=========== Daftar Produk ===========")
    for i, produk in enumerate(produk_list, 1):
        print(f"{i}. {produk.get_info()}")
    print("=====================================")

def main():
    while True:
        print("\n+==============================+")
        print("|           Main Menu          |")
        print("+==============================+")
        print("|1. Tampilkan Daftar Produk    |")
        print("|2. Tambah Produk              |")
        print("|3. Update Produk              |")
        print("|4. Hapus Produk               |")
        print("|5. Lanjutkan Transaksi        |")
        print("|0. Keluar                     |")
        print("+==============================+")

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            read_produk()
        elif pilihan == "2":
            create_produk()
        elif pilihan == "3":
            update_produk()
        elif pilihan == "4":
            delete_produk()
        elif pilihan == "5":
            nik = input("Masukkan NIK Pegawai: ")
            nama_pegawai = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai = Pegawai(nik, nama_pegawai, alamat)
            
            no_transaksi = input("Masukkan Nomor Transaksi: ")
            detail_transaksi = input("Masukkan Detail Transaksi: ")
            transaksi = Transaksi(no_transaksi, detail_transaksi)
            
            tampilkan_menu()
            pilihan_produk = int(input("Pilih produk (masukkan nomor): "))
            jumlah_produk = int(input("Masukkan jumlah produk: "))
            
            if 1 <= pilihan_produk <= len(produk_list):
                produk_terpilih = produk_list[pilihan_produk - 1]
                total_harga = produk_terpilih.harga * jumlah_produk
                struk = Struk(transaksi.no_transaksi, pegawai.nama, produk_terpilih.nama_produk, jumlah_produk, total_harga)
                
                print("\n" + struk.print_struk())
            else:
                print("Pilihan produk tidak valid!")
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
