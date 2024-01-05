import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

def dekripsi():
    # Load private key
    private_key_path = "private_key.pem"

    # Check if private key file exists
    if not os.path.exists(private_key_path):
        print("File kunci privat tidak ditemukan. Silakan buat kunci terlebih dahulu.")
        return

    with open(private_key_path, "rb") as private_key_file:
        private_key_bytes = private_key_file.read()

    private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())

    # Load encrypted text
    encrypted_text_path = "encrypted_text.bin"

    # Check if encrypted text file exists
    if not os.path.exists(encrypted_text_path):
        print("File teks terenkripsi tidak ditemukan. Silakan enkripsi terlebih dahulu.")
        return

    with open(encrypted_text_path, "rb") as encrypted_text_file:
        ciphertext = encrypted_text_file.read()

    # Decrypt the ciphertext
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Print the decrypted text
    print("Teks terenkripsi berhasil didekripsi:")
    print(plaintext.decode("utf-8"))
    
    # Menampilkan pilihan "Kembali"
    print("1. Kembali")

    # Mendapatkan input dari pengguna
    pilihan = input("Pilih: ")
    if pilihan == "1":
        return

if __name__ == "__main__":
    dekripsi()
