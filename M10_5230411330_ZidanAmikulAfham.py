import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    port=8889,
    database="pbop2"
)

cur = mydb.cursor()

while True:
    print("\n+==============================+")
    print("|           Main Menu          |")
    print("+==============================+")
    print("|1. Tambah Data                |")
    print("|2. Tampilkan Data             |")
    print("|3. Ubah Data                  |")
    print("|4. Hapus Data                 |")
    print("|0. Keluar                     |")
    print("+==============================+")
    menu = input("Pilih menu: ")

    if menu == "1":
        print("\n+==============================+")
        print("|        Sub Menu Tambah       |")
        print("+==============================+")
        print("|1. Tambah Pegawai             |")
        print("|2. Tambah Produk              |")
        print("|3. Tambah Transaksi           |")
        print("|4. Tambah Struk               |")
        print("|0. Kembali                    |")
        print("+==============================+")
        sub_menu = input("Pilih sub menu: ")

        if sub_menu == "1":
            nik = input("Masukkan NIK Pegawai: ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            cur.execute("INSERT INTO pegawai VALUES (%s, %s, %s)", (nik, nama, alamat))
            mydb.commit()
            print("Pegawai berhasil ditambahkan.")

        elif sub_menu == "2":
            kode_produk = input("Masukkan Kode Produk: ")
            nama_produk = input("Masukkan Nama Produk: ")
            jenis_produk = input("Masukkan Jenis Produk: ")
            harga = int(input("Masukkan Harga Produk: "))
            cur.execute("INSERT INTO produk VALUES (%s, %s, %s, %s)", (kode_produk, nama_produk, jenis_produk, harga))
            mydb.commit()
            print("Produk berhasil ditambahkan.")

        elif sub_menu == "3":
            no_transaksi = input("Masukkan Nomor Transaksi: ")
            detail_transaksi = input("Masukkan Detail Transaksi: ")
            cur.execute("INSERT INTO transaksi VALUES (%s, %s)", (no_transaksi, detail_transaksi))
            mydb.commit()
            print("Transaksi berhasil ditambahkan.")

        elif sub_menu == "4":
            no_transaksi = input("Masukkan Nomor Transaksi: ")
            nik_pegawai = input("Masukkan NIK Pegawai: ")
            kode_produk = input("Masukkan Kode Produk: ")
            jumlah_produk = int(input("Masukkan Jumlah Produk: "))

            cur.execute("INSERT INTO struk (no_transaksi, nik_pegawai, kode_produk, jumlah_produk) VALUES (%s, %s, %s, %s)", 
                        (no_transaksi, nik_pegawai, kode_produk, jumlah_produk))
            mydb.commit()
            print("Struk berhasil ditambahkan.")

    elif menu == "2":
        print("\n+==============================+")
        print("|       Sub Menu Tampilkan     |")
        print("+==============================+")
        print("|1. Tampilkan Pegawai          |")
        print("|2. Tampilkan Produk           |")
        print("|3. Tampilkan Transaksi        |")
        print("|4. Tampilkan Struk            |")
        print("|0. Kembali                    |")
        print("+==============================+")
        sub_menu = input("Pilih sub menu: ")

        if sub_menu == "1":
            cur.execute("SELECT * FROM pegawai")
            result = cur.fetchall()
            for row in result:
                print(row)

        elif sub_menu == "2":
            cur.execute("SELECT * FROM produk")
            result = cur.fetchall()
            for row in result:
                print(row)

        elif sub_menu == "3":
            cur.execute("SELECT * FROM transaksi")
            result = cur.fetchall()
            for row in result:
                print(row)

        elif sub_menu == "4":
            cur.execute("""
                SELECT struk.no_transaksi, pegawai.nama_pegawai, produk.nama_produk, struk.jumlah_produk, struk.total_harga
                FROM struk
                JOIN pegawai ON struk.nik_pegawai = pegawai.nik
                JOIN produk ON struk.kode_produk = produk.kode_produk
            """)
            result = cur.fetchall()
            for row in result:
                print(row)

    elif menu == "3":
        print("\n+==============================+")
        print("|        Sub Menu Ubah         |")
        print("+==============================+")
        print("|1. Ubah Pegawai               |")
        print("|2. Ubah Produk                |")
        print("|3. Ubah Transaksi             |")
        print("|4. Ubah Struk                 |")
        print("|0. Kembali                    |")
        print("+==============================+")
        sub_menu = input("Pilih sub menu: ")

        if sub_menu == "1":
            nik = input("Masukkan NIK Pegawai yang akan diubah: ")
            nama = input("Masukkan Nama Pegawai baru: ")
            alamat = input("Masukkan Alamat Pegawai baru: ")
            cur.execute("UPDATE pegawai SET nama_pegawai=%s, alamat_pegawai=%s WHERE nik=%s", (nama, alamat, nik))
            mydb.commit()
            print("Data pegawai berhasil diubah.")

        elif sub_menu == "2":
            kode_produk = input("Masukkan Kode Produk yang akan diubah: ")
            nama_produk = input("Masukkan Nama Produk baru: ")
            jenis_produk = input("Masukkan Jenis Produk baru: ")
            harga = int(input("Masukkan Harga Produk baru: "))
            cur.execute("UPDATE produk SET nama_produk=%s, jenis_produk=%s, harga_produk=%s WHERE kode_produk=%s", 
                        (nama_produk, jenis_produk, harga, kode_produk))
            mydb.commit()
            print("Data produk berhasil diubah.")

        elif sub_menu == "3":
            no_transaksi = input("Masukkan Nomor Transaksi yang akan diubah: ")
            detail_transaksi = input("Masukkan Detail Transaksi baru: ")
            cur.execute("UPDATE transaksi SET detail_transaksi=%s WHERE no_transaksi=%s", 
                        (detail_transaksi, no_transaksi))
            mydb.commit()
            print("Data transaksi berhasil diubah.")

        elif sub_menu == "4":
            no_transaksi = input("Masukkan Nomor Transaksi pada struk: ")
            kode_produk = input("Masukkan Kode Produk pada struk: ")
            jumlah_produk = int(input("Masukkan Jumlah Produk baru: "))
            cur.execute("UPDATE struk SET jumlah_produk=%s WHERE no_transaksi=%s AND kode_produk=%s", 
                        (jumlah_produk, no_transaksi, kode_produk))
            mydb.commit()
            print("Data struk berhasil diubah.")

    elif menu == "4":
        print("\n+==============================+")
        print("|        Sub Menu Hapus        |")
        print("+==============================+")
        print("|1. Hapus Pegawai              |")
        print("|2. Hapus Produk               |")
        print("|3. Hapus Transaksi            |")
        print("|4. Hapus Struk                |")
        print("|0. Kembali                    |")
        print("+==============================+")
        sub_menu = input("Pilih sub menu: ")

        if sub_menu == "1":
            nik = input("Masukkan NIK Pegawai yang akan dihapus: ")
            cur.execute("DELETE FROM pegawai WHERE nik=%s", (nik,))
            mydb.commit()
            print("Pegawai berhasil dihapus.")

        elif sub_menu == "2":
            kode_produk = input("Masukkan Kode Produk yang akan dihapus: ")
            cur.execute("DELETE FROM produk WHERE kode_produk=%s", (kode_produk,))
            mydb.commit()
            print("Produk berhasil dihapus.")

        elif sub_menu == "3":
            no_transaksi = input("Masukkan Nomor Transaksi yang akan dihapus: ")
            cur.execute("DELETE FROM transaksi WHERE no_transaksi=%s", (no_transaksi,))
            mydb.commit()
            print("Transaksi berhasil dihapus.")

        elif sub_menu == "4":
            no_transaksi = input("Masukkan Nomor Transaksi pada struk: ")
            kode_produk = input("Masukkan Kode Produk pada struk: ")
            cur.execute("DELETE FROM struk WHERE no_transaksi=%s AND kode_produk=%s", 
                        (no_transaksi, kode_produk))
            mydb.commit()
            print("Struk berhasil dihapus.")

    elif menu == "0":
        print("Keluar dari program.")
        break

cur.close()
mydb.close()
