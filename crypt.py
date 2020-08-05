from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and saves to a file `key.key`
    """
    key_ = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key_)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def encrypt(filename, key_):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes
    """
    f = Fernet(key_)
    with open(filename, "rb") as fl:
        # read all file data
        file_data = fl.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as fl:
        fl.write(encrypted_data)


def decrypt(filename, key_):
    """
    Given a filename (str) and key (bytes), it decrypts the file
    and writes original file
    """
    f = Fernet(key_)
    with open(filename, "rb") as fl:
        # read the encrypted data
        encrypted_data = fl.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as fl:
        fl.write(decrypted_data)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File Encrypt Script")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument(
        "-g",
        "--generate-key",
        dest="generate_key",
        action="store_true",
        help="Whether to generate a new key or use existing key",
    )
    parser.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        help="Whether to encrypt the file, only -e or -d can be specified.",
    )
    parser.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help="Whether to decrypt the file, only -e or -d can be specified.",
    )

    args = parser.parse_args()
    file = args.file
    generate_key = args.generate_key

    if generate_key:
        write_key()
    # load the key
    key = load_key()

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError(
            "Please specify whether you want to encrypt the file or decrypt it."
        )
    elif encrypt_:
        encrypt(file, key)
    elif decrypt_:
        decrypt(file, key)
    else:
        raise TypeError(
            "Please specify whether you want to encrypt the file or decrypt it."
        )
