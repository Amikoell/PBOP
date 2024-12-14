import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier  
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

def load_data(file_name):
    try:
        data = pd.read_excel(file_name)
        print(f"Data berhasil dimuat dari '{file_name}' dengan {data.shape[0]} baris dan {data.shape[1]} kolom.")
        return data
    except Exception as e:
        print(f"Error saat memuat file: {e}")
        return None

def handle_missing_values(data):
    print("\n=== Penanganan Missing Values ===")
    print("1. Isi dengan rata-rata (mean)")
    print("2. Isi dengan median")
    print("3. Isi dengan modus")
    print("4. Hapus baris dengan nilai kosong")
    choice = input("Pilih metode penanganan: ")

    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = data.select_dtypes(include=['object']).columns

    if choice == "1":
        imputer = SimpleImputer(strategy="mean")
        data[numeric_cols] = imputer.fit_transform(data[numeric_cols])
        print("Missing values telah diisi dengan rata-rata.")
    elif choice == "2":
        imputer = SimpleImputer(strategy="median")
        data[numeric_cols] = imputer.fit_transform(data[numeric_cols])
        print("Missing values telah diisi dengan median.")
    elif choice == "3":
        imputer = SimpleImputer(strategy="most_frequent")
        data[categorical_cols] = imputer.fit_transform(data[categorical_cols])
        data[numeric_cols] = imputer.fit_transform(data[numeric_cols])
        print("Missing values telah diisi dengan modus.")
    elif choice == "4":
        data.dropna(inplace=True)
        print("Baris dengan missing values telah dihapus.")
    else:
        print("Pilihan tidak valid! Tidak ada perubahan pada data.")
    
    return data

def run_analysis(data, algorithm, test_size=0.2):
    X = data.iloc[:, :-1]  
    y = data.iloc[:, -1]   

    if y.dtype == 'object' or isinstance(y.iloc[0], str):
        print("Target adalah data kategorikal. Mengonversi ke numerik...")
        le = LabelEncoder()
        y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    if algorithm == "naive_bayes":
        model = GaussianNB()
    elif algorithm == "decision_tree":
        model = DecisionTreeClassifier()
    elif algorithm == "neural_network":
        model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
    elif algorithm == "knn":
        model = KNeighborsClassifier()
    else:
        print("Algoritma tidak dikenali!")
        return

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"\nModel: {algorithm}")
    print(f"Akurasi: {accuracy:.4f}")

def main():
    print("=== Masukkan Nama File Data ===")
    file_name = input("Masukkan nama file (misal: datasets/air_quality.xlsx): ")
    data = load_data(file_name)

    if data is None:
        print("Tidak dapat melanjutkan tanpa data yang valid.")
        return

    while True:
        print("\n+==============================+")
        print("|           Main Menu          |")
        print("+==============================+")
        print("|1. Preprocessing Data         |")
        print("|2. Analisis Data              |")
        print("|3. Keluar                     |")
        print("+==============================+")
        choice = input("Pilih opsi: ")

        if choice == "1":
            print(data.head())
            print("\n=== Menu Preprocessing ===")
            print("1. Tampilkan Data")
            print("2. Tangani Missing Values")
            sub_choice = input("Pilih opsi preprocessing: ")

            if sub_choice == "1":
                print(data.info())
            elif sub_choice == "2":
                data = handle_missing_values(data)
            else:
                print("Pilihan tidak valid!")

        elif choice == "2":
            if data is None:
                print("Data belum dimuat! Silakan lakukan preprocessing terlebih dahulu.")
                continue

            print("\nPilih algoritma:")
            print("1. Naive Bayes")
            print("2. Decision Tree")
            print("3. Neural Network (MLPClassifier)")
            print("4. K-Nearest Neighbors (KNN)")
            algo_choice = input("Pilih opsi algoritma: ")

            algo_map = {
                "1": "naive_bayes",
                "2": "decision_tree",
                "3": "neural_network",
                "4": "knn"
            }
            algorithm = algo_map.get(algo_choice)
            if not algorithm:
                print("Pilihan algoritma tidak valid!")
                continue

            try:
                test_size_input = input("Masukkan test size (default 0.2): ")
                test_size = float(test_size_input) if test_size_input else 0.2
                if not (0 < test_size < 1):
                    raise ValueError("Test size harus di antara 0 dan 1.")
            except ValueError as e:
                print(f"Input tidak valid: {e}")
                test_size = 0.2  

            run_analysis(data, algorithm, test_size)

        elif choice == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
