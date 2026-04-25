import src.utils.paths as paths
import src.crypto.crypto as crypto

def path_test():
    print(f"base_path: {paths.get_base_path()}")
    print(f"")
    print(f"get_app_data_dir: {paths.get_app_data_dir()}")
    print(f"get_config_data_dir: {paths.get_config_data_dir()}")
    print(f"get_cache_data_dir: {paths.get_cache_data_dir()}")
    print(f"")
    print(f"get_database_path: {paths.get_database_path()}")
    print(f"get_salt_path: {paths.get_salt_path()}")
    print(f"get_config_path: {paths.get_config_path()}")
    print(f"get_log_path: {paths.get_log_path()}")

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

def run_crypto_test():
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