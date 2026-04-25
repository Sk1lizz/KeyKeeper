# src\utils\paths.py

"""Управление путями к файлам и папкам"""

import sys
import os
from pathlib import Path


# ===================================================
# Базовые пути
# ===================================================

def get_base_path() -> Path:
    """ Возвращает путь до файлов проекта """

    if getattr(sys, "frozen", False): # Если проект собран, то возвращает путь до временной папки
        return Path(sys._MEIPASS)
    
    else: # Если проект запрускается через .py, то вернут путь до проекта
        return Path(__file__).parent.parent.parent


def get_resource_path(relative_path: str) -> Path:
    """ Возвращает путь до необходимого ресурса """

    return get_base_path() / "resources" / relative_path


# ===================================================
# Пути до определенных файлов
# ===================================================

def get_icon_path(icon_name: str) -> str:
    """ Возвращает путь до иконки """

    return get_resource_path(relative_path=f"icons/{icon_name}")


def get_theme_path(theme_name: str) -> str:
    """ Возвращает путь до файла со стилями для приложения """

    return get_resource_path(relative_path=f"styles/{theme_name}")


def get_translation_path(translation_name: str) -> str:
    """ Возвращает путь до файла перевода """

    return get_resource_path(relative_path=f"translations/{translation_name}")


# ===================================================
# Пути для пользовательских данных
# ===================================================

def get_app_data_dir() -> Path:
    """ Пути до папки с данными """

    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".local" / "share"))

    app_dir = base / "KeyKeeper"

    app_dir.mkdir(parents=True, exist_ok=True)

    return app_dir


def get_config_data_dir() -> Path:
    """ Путь до папки с конфигом """

    if sys.platform == "win32":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Preferences"
    
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))

    config_dir = base / "KeyKeeper"

    config_dir.mkdir(parents=True, exist_ok=True)

    return config_dir


def get_cache_data_dir() -> Path:
    """ Путь до папки кэша"""

    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Caches"
    
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".cache"))

    cache_dir = base / "KeyKeeper" / "cache"

    cache_dir.mkdir(parents=True, exist_ok=True)

    return cache_dir


# ===================================================
# Пути к конкретным файлам
# ===================================================

def get_database_path() -> Path:
    """ Путь до бд с данными """

    return get_app_data_dir() / "data.db"


def get_salt_path() -> Path:
    """ Путь до соли """

    return get_app_data_dir() / "salt.bin"


def get_config_path() -> Path:
    """ Путь до конфига """

    return get_config_data_dir() / "config.yaml"


def get_log_path() -> Path:
    """ Путь до логов """

    return get_app_data_dir() / "keykeeper.log"