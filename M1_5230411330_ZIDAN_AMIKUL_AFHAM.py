def menu():
    print("\n|| Perhitungan Matematika Bangun Ruang ")
    print("\n+==================+")
    print("|        MENU        |")
    print("+====================+")
    print("|1. Bangun Ruang 2D  |")
    print("|2. Bangun Ruang 3D  |")
    print("|0. Keluar           |")
    print("+====================+")

def persegi(s):
    luas = s ** 2
    keliling = 4 * s
    return luas, keliling

def persegi_panjang(p, l):
    luas = p * l
    keliling = 2 * (p + l)
    return luas, keliling

def lingkaran(r):
    phi = 3.14
    luas = phi * r**2
    keliling = 2 * phi * r
    return luas, keliling
    
def kubus(s):
    volume = s**3
    luas_permukaan = 6 * s**2    
    return volume, luas_permukaan

def balok(p, t, l):
    volume = p * l * t
    luas_permukaan = 2*( p*l + p*t + l*t) 
    return volume, luas_permukaan

def tabung(r, t):
    phi = 3.14
    volume = phi * r**2 * t
    luas_permukaan = 2 * phi * r * (r + t)
    return volume, luas_permukaan

def main():
    while True :
        menu()
        pilihMenu = input("\n>> Masukkan Pilihan Menu: ")
        if pilihMenu == "1":
            while True:
                print("\n+==================+")
                print("|         2D         |")
                print("+====================+")
                print("|1. Persegi          |")
                print("|2. Persegi Panjang  |")
                print("|3. Lingkaran        |")
                print("|0. Kembali          |")
                print("+====================+")
                pilih = input("\n>> Masukkan Pilihan Menu: ")
                if pilih== "1":
                    s = float(input("Masukkan sisi (cm): "))
                    luas, keliling = persegi(s)
                    print(">>")
                    print(f"Luas Persegi: {luas:.2f}")
                    print(f"Keliling Persegi: {keliling:.2f}")
                elif pilih== "2":
                    p = float(input("Masukkan panjang (cm): "))
                    l = float(input("Masukkan lebar (cm): "))
                    luas, keliling = persegi_panjang(p, l)
                    print(">>")
                    print(f"Luas Persegi panjang: {luas:.2f}")
                    print(f"Keliling Persegi Panjang: {keliling:.2f}")
                elif pilih== "3":
                    r = float(input("Masukkan jari-jari lingkaran / r: "))
                    luas, keliling = lingkaran(r)
                    print(">>")
                    print(f"Luas Lingkaran: {luas:.2f}")
                    print(f"Keliling Lingkaran: {keliling:.2f}")
                elif pilih == "0":
                    break
                else:
                    print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")
        
        elif pilihMenu == "2":
            while True:
                print("\n+==================+")
                print("|         2D         |")
                print("+====================+")
                print("|1. Kubus            |")
                print("|2. Balok            |")
                print("|3. Tabung           |")
                print("|0. Kembali          |")
                print("+====================+")
                pilih = input("\n>> Masukkan Pilihan Menu: ")
                if pilih== "1":
                    s = float(input("Masukkan sisi (cm): "))
                    volume, luas_permukaan = kubus(s)
                    print(">>")
                    print(f"Volume Kubus: {volume:.2f}")
                    print(f"Luas Permukaan Kubus: {luas_permukaan:.2f}")
                elif pilih== "2":
                    p = float(input("Masukkan panjang (cm): "))
                    t = float(input("Masukkan tinggi (cm): "))
                    l = float(input("Masukkan lebar (cm): "))
                    volume, luas_permukaan = balok(p, t, l)
                    print(">>")
                    print(f"Volume Balok: {volume:.2f}")
                    print(f"Luas Permukaan Balok: {luas_permukaan:.2f}")
                elif pilih== "3":
                    r = float(input("Masukkan jari-jari lingkaran / r: "))
                    t = float(input("Masukkan tinggi: "))
                    volume, luas_permukaan = tabung(r, t)
                    print(">>")
                    print(f"Volume Tabung: {volume:.2f}")
                    print(f"Luas Permukaan Tabung: {luas_permukaan:.2f}")
                elif pilih == "0":
                    break
                else:
                    print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")
        
        elif pilihMenu == "0":
            print("\n>>> Terimakasih, Program telah keluar. <<<")
            break
        
        else :
            print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")
                    
                    
if __name__ == "__main__":
    main()