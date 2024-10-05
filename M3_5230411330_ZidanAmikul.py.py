class daftar_menu:
    daftar_makanan = []
    daftar_minuman = []

    def menu():
        print("\n+=======================+")
        print("|          MENU         |")
        print("+=======================+")
        print("|1. Lihat Daftar Makan  |")
        print("|2. Lihat Daftar Minuman|")
        print("|3. Tambah Menu         |")
        print("|0. Keluar              |")
        print("+=======================+")

    def list_makan():
        if not daftar_menu.daftar_makanan:
            print("\nBelum ada makanan yang ditambahkan.")
        else:
            print("\n+=======================+")
            print("|     Daftar Makanan    |")
            print("+=======================+")
            for i, (makanan, harga) in enumerate(daftar_menu.daftar_makanan, start=1):
                print(f"|{i}. {makanan} : Rp {harga:,.2f} |")
            print("+=======================+")

    def list_minum():
        if not daftar_menu.daftar_minuman:
            print("\nBelum ada minuman yang ditambahkan.")
        else:
            print("\n+===========================+")
            print("|       Daftar Minuman      |")
            print("+===========================+")
            for i, (minuman, harga) in enumerate(daftar_menu.daftar_minuman, start=1):
                print(f"|{i}. {minuman} : Rp {harga:,.2f} |")
            print("+===========================+")

class tambah_menu:
    def add_makanan():
        while True:
            add_m = input("Masukkan nama makanan baru (atau '0' untuk kembali): ")
            if add_m == '0':
                break
            elif not add_m.isalpha():
                print("Input tidak valid.")
            else:
                try:
                    harga = float(input(f"Masukkan harga untuk {add_m}: "))
                    daftar_menu.daftar_makanan.append((add_m, harga))
                    print(f"{add_m} dengan harga {harga} telah ditambahkan ke daftar makanan.")
                except ValueError:
                    print("Input tidak valid. Harga harus berupa angka.")
                
    def add_minuman():
        while True:
            add_m2 = input("Masukkan nama minuman baru (atau '0' untuk kembali): ")
            if add_m2 == '0':
                break
            elif not add_m2.isalpha():
                print("Input tidak valid.")
            else:
                try:
                    harga = float(input(f"Masukkan harga untuk {add_m2}: "))
                    daftar_menu.daftar_minuman.append((add_m2, harga))
                    print(f"{add_m2} dengan harga {harga} telah ditambahkan ke daftar minuman.")
                except ValueError:
                    print("Input tidak valid. Harga harus berupa angka.")

while True:
    daftar_menu.menu()
    pilihan = input("Masukkan pilihan: ")
    if pilihan == '1':
        daftar_menu.list_makan()
    elif pilihan == '2':
        daftar_menu.list_minum()
    elif pilihan == '3':
        print("\n+===========================+")
        print("|    Menu Yang di tambah    |")
        print("+===========================+")
        print("|1. Tambahkan Makanan       |")
        print("|2. Tambahkan Minuman       |")
        print("|0. Keluar                  |")
        print("+===========================+")
        sub_pilihan = input("Masukkan Pilihan :  ")
        if sub_pilihan == '1':
            tambah_menu.add_makanan()
        elif sub_pilihan == '2':
            tambah_menu.add_minuman()
        else:
            print("Pilihan tidak valid.")
    elif pilihan == '0':
        print("Keluar dari sistem...")
        break
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")
