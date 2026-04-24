# src\utils\paths.py

"""Управление путями к файлам и папкам"""

import sys
import os
from pathlib import Path


# ===================================================
# Базовые пути
# ===================================================

def get_base_path() -> Path:
    """"""

    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    
    else:
        return Path(__file__).parent.parent.parent


def get_resource_path(relative_path: str) -> Path:
    """"""

    return get_base_path() / "resources" / relative_path


# ===================================================
# Пути до определенных файлов
# ===================================================

def get_icon_path(icon_name: str) -> str:
    """"""

    return get_resource_path(relative_path=f"icons/{icon_name}")


def get_theme_path(theme_name: str) -> str:
    """"""

    return get_resource_path(relative_path=f"styles/{theme_name}")


def get_translation_path(translation_name: str) -> str:
    """"""

    return get_resource_path(relative_path=f"translations/{translation_name}")


# ===================================================
# Пути для пользовательских данных
# ===================================================

def get_app_data_dir() -> Path:
    """"""

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
    """"""

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
    """"""

    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Caches"
    
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".cache"))

    cache_dir = base / "KeyKeeper" / "cache"

    cache_dir.mkdir(parents=True, exist_ok=True)

    return cache_dir