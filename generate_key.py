import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def generate_key():
    # Simpan direktori saat ini
    current_directory = os.getcwd()

    # Ubah direktori kerja ke tempat generate_key.py berada
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Get public key from private key
    public_key = private_key.public_key()

    # Serialize private key to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Bangun jalur lengkap ke generate_key.py
    generate_key_path = os.path.join(script_directory, "generate_key.py")

    # Simpan private key dan public key ke file
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_key_pem)

    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key_pem)

    # Kembalikan direktori kerja ke direktori awal
    os.chdir(current_directory)

    print("Kunci privat dan kunci publik telah berhasil dibuat dan disimpan.")
    
    # Menampilkan pilihan "Kembali"
    print("1. Kembali")

    # Mendapatkan input dari pengguna
    pilihan = input("Pilih: ")
    if pilihan == "1":
        return

if __name__ == "__main__":
    generate_key()
