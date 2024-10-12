class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama  
        self.__ktp = ktp 
        self._limit_pinjaman = limit_pinjaman 

    def tampilkan_debitur(self):
        print(f"Nama: {self.nama}")
        print(f"KTP: {self.__ktp}")  
        print(f"Limit Pinjaman: {self._limit_pinjaman}")
        print("---------------------------")

    def cari_debitur(self, nama):
        if self.nama.lower() == nama.lower():
            self.tampilkan_debitur()
            return True
        return False

    def cek_ktp(self, ktp):
        return self.__ktp == ktp

class Pinjaman(Debitur):
    def __init__(self, nama, ktp, limit_pinjaman, pinjaman=None, bunga=None, bulan=None):
        super().__init__(nama, ktp, limit_pinjaman)
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan

    def tambah_pinjaman(self, pinjaman, bunga, bulan):
        if pinjaman > self._limit_pinjaman:
            print("!! Validasi gagal: Pinjaman melebihi limit pinjaman !!")
        else:
            self.pinjaman = pinjaman
            self.bunga = bunga
            self.bulan = bulan
            print(f"Pinjaman berhasil ditambahkan untuk {self.nama}.")

    def tampilkan_pinjaman(self):
        if self.pinjaman and self.bunga and self.bulan:
            angsuran_pokok = self.pinjaman * (self.bunga / 100)
            angsuran_bulanan = angsuran_pokok / self.bulan
            total_angsuran = angsuran_pokok + angsuran_bulanan

            print(f"\n>> Rincian Pinjaman atas nama {self.nama} <<")
            print(f"Pinjaman: {self.pinjaman}")
            print(f"Bunga: {self.bunga}%")
            print(f"Bulan: {self.bulan}")
            print(f"Angsuran Bulanan: {angsuran_bulanan:.2f}")
            print(f"Total Angsuran: {total_angsuran:.2f}")
            print("------------------------------------\n")
        else:
            print(f"Tidak ada pinjaman yang terdaftar atas nama {self.nama}.")


def kelola_debitur(daftar_debitur):
    while True:
        print("\n+============================+")
        print("|       Kelola Debitur       |")
        print("+============================+")
        print("|1. Tampilkan Semua Debitur  |")
        print("|2. Cari Debitur             |")
        print("|3. Tambah Debitur           |")
        print("|0. Kembali                  |")
        print("+============================+")

        pilihan = input(">> Masukkan Pilihan Sub Menu: ")

        if pilihan == '1':
            print("\n>> Daftar Semua Debitur <<")
            if not daftar_debitur:
                print("Tidak ada debitur yang terdaftar.")
            for debitur in daftar_debitur:
                debitur.tampilkan_debitur()

        elif pilihan == '2':
            nama_cari = input(">> Masukkan nama debitur yang dicari: ")
            ditemukan = False
            for debitur in daftar_debitur:
                if debitur.cari_debitur(nama_cari):
                    ditemukan = True
                    break
            if not ditemukan:
                print(f"Debitur dengan nama {nama_cari} tidak ditemukan.")

        elif pilihan == '3':
            nama = input(">> Masukkan nama debitur: ")
            ktp = input(">> Masukkan KTP debitur: ")
            limit_pinjaman = float(input(">> Masukkan limit pinjaman debitur: "))
            for debitur in daftar_debitur:
                if debitur.cek_ktp(ktp):
                    print("Validasi gagal: Debitur dengan KTP ini sudah ada!")
                    break
            else:
                debitur_baru = Pinjaman(nama, ktp, limit_pinjaman)
                daftar_debitur.append(debitur_baru)
                print(f"Debitur {nama} berhasil ditambahkan.")

        elif pilihan == '0':
            print("Kembali ke menu utama.")
            break

        else:
            print("!! Pilihan tidak valid. Coba lagi !!")


def kelola_pinjaman(daftar_debitur):
    while True:
        print("\n+===========================+")
        print("|      Kelola Pinjaman      |")
        print("+===========================+")
        print("|1. Tambah Pinjaman         |")
        print("|2. Tampilkan Semua Pinjaman|")
        print("|0. Kembali                 |")
        print("+===========================+")
        
        pilihan = input(">> Masukkan Pilihan Sub Menu: ")

        if pilihan == '1':
            nama_cari = input(">> Masukkan nama debitur yang akan diberi pinjaman: ")
            ditemukan = False
            for debitur in daftar_debitur:
                if debitur.cari_debitur(nama_cari):
                    pinjaman = float(input(">> Masukkan jumlah pinjaman: "))
                    bunga = float(input(">> Masukkan persentase bunga: "))
                    bulan = int(input(">> Masukkan jumlah bulan untuk cicilan: "))
                    debitur.tambah_pinjaman(pinjaman, bunga, bulan)
                    ditemukan = True
                    break
            if not ditemukan:
                print(f"Debitur dengan nama {nama_cari} tidak ditemukan.")

        elif pilihan == '2':
            print("\nDaftar Semua Pinjaman:")
            if not daftar_debitur:
                print("Tidak ada debitur yang terdaftar.")
            for debitur in daftar_debitur:
                debitur.tampilkan_pinjaman()

        elif pilihan == '0':
            print("Kembali ke menu utama.")
            break

        else:
            print("!! Pilihan tidak valid. Coba lagi !!")


def main():
    daftar_debitur = []

    while True:
        print("\n+=========================+")
        print("|     Aplikasi Pinjol     |")
        print("+=========================+")
        print("|1. Kelola Debitur        |")
        print("|2. Kelola Pinjaman       |")
        print("|0. Keluar                |")
        print("+=========================+")

        pilihan = input(">> Masukkan Pilihan Menu Utama: ")

        if pilihan == '1':
            kelola_debitur(daftar_debitur)

        elif pilihan == '2':
            kelola_pinjaman(daftar_debitur)

        elif pilihan == '0':
            print("Keluar dari sistem.")
            break

        else:
            print("!!  Pilihan tidak valid. Coba lagi !!")


if __name__ == "__main__":
    main()
