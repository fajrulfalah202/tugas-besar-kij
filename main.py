import os
from generate_key import generate_key
from enkripsi import enkripsi
from dekripsi import dekripsi

def clear_all_files():
    try:
        os.remove("encrypted_text.bin")
        os.remove("private_key.pem")
        os.remove("public_key.pem")
        print("Semua file berhasil dihapus.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def main():
    while True:
        print("\nImplementasi Algoritma RSA:")
        print("1. Generate Key")
        print("2. Enkripsi")
        print("3. Dekripsi")
        print("0. Clear All")
        pilihan = input("Pilih: ")
        
        try:
            pilihan = int(pilihan)
            if pilihan == 1:
                generate_key()
            elif pilihan == 2:
                enkripsi()
            elif pilihan == 3:
                dekripsi()
            elif pilihan == 0:
                clear_all_files()
            else:
                print("Pilihan tidak valid. Silakan masukkan nomor 0, 1, 2, atau 3.")
        except ValueError:
            print("Masukkan nomor yang valid.")

if __name__ == "__main__":
    main()
