# src\utils\paths.py

"""Управление путями к файлам и папкам"""

import sys
import os
from pathlib import Path

def get_base_path() -> Path:
    """"""

    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    
    else:
        return Path(__file__).parent.parent.parent