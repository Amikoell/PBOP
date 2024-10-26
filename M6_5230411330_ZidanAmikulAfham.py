class Order:
    def __init__(self, order_id, name, details):
        self.order_id = order_id
        self.name = name
        self.details = details

    def display_order(self):
        print(f"ID Pesanan: {self.order_id} | Nama: {self.name} | Detail: {self.details}")


class Delivery:
    def __init__(self, delivery_id, name, information, date, address):
        self.delivery_id = delivery_id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self, order):
        print(f"\nMemproses pengiriman untuk Pesanan '{order.name}':")
        print(f"ID Pengiriman: {self.delivery_id} | Nama: {self.name}")
        print(f"Informasi: {self.information}")
        print(f"Tanggal (hh/bb/tt): {self.date}")
        print(f"Alamat: {self.address}\n")

    def display_delivery(self):
        print(f"ID Pengiriman: {self.delivery_id} | Nama: {self.name} | Informasi: {self.information}")
        print(f"Tanggal: {self.date} | Alamat: {self.address}")


def menu_utama():
    orders = []
    deliveries = []

    while True:
        print("\n+==============================+")
        print("|           Main Menu          |")
        print("+==============================+")
        print("|1. Buat pesanan baru          |")
        print("|2. Tampilkan semua pesanan    |")
        print("|3. Buat pengiriman baru       |")
        print("|4. Tampilkan semua pengiriman |")
        print("|5. Proses pengiriman          |")
        print("|0. Keluar                     |")
        print("+==============================+")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            order_id = input("Masukkan ID Pesanan: ")
            name = input("Masukkan Nama Pesanan: ")
            details = input("Masukkan Detail Pesanan: ")
            orders.append(Order(order_id, name, details))
            print("Pesanan berhasil dibuat!")

        elif pilihan == '2':
            if not orders:
                print("Tidak ada pesanan yang tersedia.")
            else:
                print("\nDaftar Pesanan:")
                for order in orders:
                    order.display_order()

        elif pilihan == '3':
            delivery_id = input("Masukkan ID Pengiriman: ")
            name = input("Masukkan Nama Pengiriman: ")
            information = input("Masukkan Informasi Pengiriman: ")
            date = input("Masukkan Tanggal Pengiriman (hh/bb/tt): ")
            address = input("Masukkan Alamat Pengiriman: ")
            deliveries.append(Delivery(delivery_id, name, information, date, address))
            print("Pengiriman berhasil dibuat!")

        elif pilihan == '4':
            if not deliveries:
                print("Tidak ada pengiriman yang tersedia.")
            else:
                print("\nDaftar Pengiriman:")
                for delivery in deliveries:
                    delivery.display_delivery()

        elif pilihan == '5':
            if not orders:
                print("Tidak ada pesanan yang tersedia.")
                continue
            if not deliveries:
                print("Tidak ada pengiriman yang tersedia.")
                continue

            print("\nPilih Pesanan:")
            for i, order in enumerate(orders):
                print(f"{i + 1}. {order.name} (ID: {order.order_id})")
            try:
                idx_order = int(input("Nomor Pesanan: ")) - 1
                selected_order = orders[idx_order]
            except (IndexError, ValueError):
                print("Nomor pesanan tidak valid.")
                continue

            print("\nPilih Pengiriman:")
            for i, delivery in enumerate(deliveries):
                print(f"{i + 1}. {delivery.name} (ID: {delivery.delivery_id})")
            try:
                idx_delivery = int(input("Nomor Pengiriman: ")) - 1
                selected_delivery = deliveries[idx_delivery]
            except (IndexError, ValueError):
                print("Nomor pengiriman tidak valid.")
                continue

            selected_delivery.process_delivery(selected_order)

        elif pilihan == '0':
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    menu_utama()
