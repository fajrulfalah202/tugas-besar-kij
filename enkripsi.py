import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def enkripsi():
    # Load public key
    public_key_path = "public_key.pem"

    # Check if public key file exists
    if not os.path.exists(public_key_path):
        print("File kunci publik tidak ditemukan. Silakan buat kunci terlebih dahulu.")
        return

    with open(public_key_path, "rb") as public_key_file:
        public_key_bytes = public_key_file.read()

    public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

    # Get plaintext from user
    plaintext = input("Masukkan teks yang akan dienkripsi: ").encode("utf-8")

    # Encrypt the plaintext
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted text to file
    with open("encrypted_text.bin", "wb") as encrypted_text_file:
        encrypted_text_file.write(ciphertext)

    print("Enkripsi berhasil. Teks terenkripsi disimpan dalam file 'encrypted_text.bin'.")
    
    # Menampilkan pilihan "Kembali"
    print("1. Kembali")

    # Mendapatkan input dari pengguna
    pilihan = input("Pilih: ")
    if pilihan == "1":
        return

if __name__ == "__main__":
    enkripsi()
