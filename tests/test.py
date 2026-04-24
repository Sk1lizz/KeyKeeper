import src.utils.paths as paths

def path_test():
    print(f"base_path: {paths.get_base_path()}")
    print(f"")
    print(f"get_app_data_dir: {paths.get_app_data_dir()}")
    print(f"get_config_data_dir: {paths.get_config_data_dir()}")
    print(f"get_cache_data_dir: {paths.get_cache_data_dir()}")