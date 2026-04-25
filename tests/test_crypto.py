import src.crypto.crypto as crypto

def crypto_test(password: str, master: str = "master-key", number: int = 0):
    manager = crypto.CryptoManager

    salt = manager.generate_salt()
    key = manager.derive_key(password=master, salt=salt)

    encrypt = manager.encrypt(data=password, key=key)
    print(f"encypt: {encrypt}")

    decrypt = manager.decrypt(data=encrypt, key=key)
    print(f"decypt: {decrypt}")
    
    assert password == decrypt

    print(f"Test №{number} - successful\n")

def main():
    password_data = [
        "password",
        "123123",
        "Edsfjklskjdf",
        "skilizz",
        "cfif",
        "encrypt",
        "decrypt"
    ]

    count = 1

    for password in password_data:
        print(f"Password: {password}\nNumber: {count}\n")
        crypto_test(password=password, number=count)
        count += 1