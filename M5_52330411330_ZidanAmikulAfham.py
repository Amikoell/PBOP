
class Music:
    def __init__(self, title, singer, genre):
        self.title = title
        self.singer = singer
        self.genre = genre

class DisplayMusic:
    def __init__(self, music_list):
        self.music_list = music_list

    def display_all(self):
        print("\n================== List All Songs ==================")
        print("Judul".ljust(20), "Penyanyi".ljust(20), "Genre")
        print("----------------------------------------------------")
        self.music_list.sort(key=lambda x: x.title)  
        for music in self.music_list:
            print(music.title.ljust(20), music.singer.ljust(20), music.genre)
        print("====================================================\n")

    def display_by_genre(self, genre):
        print(f"\n================== {genre} Songs ==================")
        print("Judul".ljust(20), "Penyanyi".ljust(20), "Genre")
        print("---------------------------------------------------")
        songs_by_genre = [music for music in self.music_list if music.genre == genre]
        if songs_by_genre:
            for music in songs_by_genre:
                print(music.title.ljust(20), music.singer.ljust(20), music.genre)
        else:
            print(f"No songs found in {genre} genre.")
        print("===================================================\n")

    def search_by_singer(self, singer_name):
        found = [music for music in self.music_list if music.singer.lower() == singer_name.lower()]
        if found:
            print(f"\nMusic by {singer_name}:")
            for music in found:
                print(f"Title: {music.title}, Genre: {music.genre}")
        else:
            print(f"No music found by {singer_name}")

class AddMusic:
    def __init__(self, music_list):
        self.music_list = music_list

    def add_music(self, title, singer, genre):
        new_music = Music(title, singer, genre)
        self.music_list.append(new_music)
        print(f"Added: {title} by {singer} (Genre: {genre})")

class DeleteMusic:
    def __init__(self, music_list):
        self.music_list = music_list

    def delete_music(self, title, genre):
        music_found = False
        for music in self.music_list:
            if music.title.lower() == title.lower() and music.genre == genre:
                self.music_list.remove(music)
                music_found = True
                print(f"Deleted: {title} from {genre} genre.")
                break
        if not music_found:
            print(f"No song with title '{title}' found in {genre} genre.")

def pop_menu():
    while True:
        print("\n+============================+")
        print("|          Pop Song          |")
        print("+============================+")
        print("|1. Display Song             |")
        print("|2. Add Song                 |")
        print("|3. Delete Song              |")
        print("|0. Kembali                  |")
        print("+============================+")
        pilihan = input(" >> Masukan Pilihan Sub Menu Pop Song: ")

        if pilihan == "1":
            display_music.display_by_genre("Pop")
        elif pilihan == "2":
            title = input("Masukan Judul Lagu: ")
            singer = input("Masukan Penyanyi: ")
            genre = "Pop"
            add_music.add_music(title, singer, genre)
        elif pilihan == "3":
            title = input("Masukan Judul Lagu yang Ingin Dihapus: ")
            delete_music.delete_music(title, "Pop")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

def rock_menu():
    while True:
        print("\n+============================+")
        print("|          Rock Song         |")
        print("+============================+")
        print("|1. Display Song             |")
        print("|2. Add Song                 |")
        print("|3. Delete Song              |")
        print("|0. Kembali                  |")
        print("+============================+")
        pilihan = input(" >> Masukan Pilihan Sub Menu Rock Song: ")

        if pilihan == "1":
            display_music.display_by_genre("Rock")
        elif pilihan == "2":
            title = input("Masukan Judul Lagu: ")
            singer = input("Masukan Penyanyi: ")
            genre = "Rock"
            add_music.add_music(title, singer, genre)
        elif pilihan == "3":
            title = input("Masukan Judul Lagu yang Ingin Dihapus: ")
            delete_music.delete_music(title, "Rock")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

def hip_hop_menu():
    while True:
        print("\n+============================+")
        print("|         Hip Hop Song       |")
        print("+============================+")
        print("|1. Display Song             |")
        print("|2. Add Song                 |")
        print("|3. Delete Song              |")
        print("|0. Kembali                  |")
        print("+============================+")
        pilihan = input(" >> Masukan Pilihan Sub Menu Hip Hop Song: ")

        if pilihan == "1":
            display_music.display_by_genre("Hip Hop")
        elif pilihan == "2":
            title = input("Masukan Judul Lagu: ")
            singer = input("Masukan Penyanyi: ")
            genre = "Hip Hop"
            add_music.add_music(title, singer, genre)
        elif pilihan == "3":
            title = input("Masukan Judul Lagu yang Ingin Dihapus: ")
            delete_music.delete_music(title, "Hip Hop")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

def main_menu():
    while True:
        print("\n+============================+")
        print("|          My Music          |")
        print("+============================+")
        print("|1. Pop Song                 |")
        print("|2. Rock Song                |")
        print("|3. Hip Hop Song             |")
        print("|4. Display All              |")
        print("|5. Search Music             |")
        print("|0. Keluar                   |")
        print("+============================+")

        pilihan = input(" >> Masukan Pilihan Menu: ")

        if pilihan == "1":
            pop_menu()
        elif pilihan == "2":
            rock_menu()
        elif pilihan == "3":
            hip_hop_menu()
        elif pilihan == "4":
            display_music.display_all()
        elif pilihan == "5":
            singer_name = input("Masukan Penyanyi yg Ingin Di Cari: ")
            display_music.search_by_singer(singer_name)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

music_list = [
    Music("Sprinter.", "Central Cee", "Hip Hop"),
    Music("Kenangan Terindah", "Samsons", "Pop"),
    Music("Bohemian Rhapsody", "Queen", "Rock"),
    Music("Lose Yourself", "Eminem", "Hip Hop"),
    Music("Rolling in the Deep", "Adele", "Pop"),
    Music("Stairway to Heaven", "Led Zeppelin", "Rock"),
    Music("Kangen", "Dewa 19", "Pop"),
    Music("Dat Stick.", "Rich Brian", "Hip Hop"),
    Music("A Day in The Live", "The Beatles", "Rock"),
    Music("Love Your Self", "Justin Bieber", "Pop"),
]

display_music = DisplayMusic(music_list)
add_music = AddMusic(music_list)
delete_music = DeleteMusic(music_list)

main_menu()
