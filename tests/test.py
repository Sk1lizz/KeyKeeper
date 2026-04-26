import src.utils.paths as paths

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