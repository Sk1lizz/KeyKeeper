# src\utils\constants.py

""" Файл с константами проекта """


# ===================================================
# Приложение
# ===================================================

APP_NAME = "KeyKeeper"
APP_VERSION = "1.0.0"
APP_AUTHOR = [
    "skilizz"
]
APP_YEAR = "2026"
APP_URL = "https://github.com/Sk1lizz/KeyKeeper"


# ===================================================
# Настройки логирования
# ===================================================

LOG_CONSOLE_LEVEL = 20
LOG_FILE_LEVEL = 10

LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_FILE = "keykeeper.log"

LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUP_COUNT = 10               # На релизе изменить на 3/5