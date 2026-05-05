# 

"""  """

import yaml
from pathlib import Path
from typing import Optional, Any, Dict, Tuple, Dict, List

from src.utils.constants import DEFAULT_LANGUAGE

from src.utils.paths import get_translation_path
from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)


class Translator:
    """"""

    _instance: Optional[Translator] = None

    def __new__(cls, lang_code: Optional[str] = None) -> "Translator":
        """"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    

    def __init__(self, lang_code: Optional[str] = None):
        """"""

        if not hasattr(self, "_initialized"):
            self._lang: str = lang_code or self._set_default_language()
            self._data: Dict[str, Any] = {}
            self._load()
            self._initialized = True
            info(f"Translator инициализирован: {self._lang}")


    def _set_default_language(self) -> str:
        """"""

        return DEFAULT_LANGUAGE
    

    def _load(self) -> None:
        """"""

        path = get_translation_path(self._lang)
        
        if not path.exists():
            warning(f"Файл с переводом не найден: {path}")
            self._data = {}
            return
        
        try:
            with open(path, "r", encoding="utf-8") as file:
                self._data = yaml.safe_load(file) or {}
            
            debug(f"Загружен перевод {self._lang} ({len(self._data)} ключей)")

        except yaml.YAMLError as e:
            error(f"Ошибка парсинга YAML {self._lang}: {e}")
            self._data = {}

        except Exception as e:
            error(f"Ошибка загрузки перевода {self._lang}: {e}")
            self._data = {}


    def get(self, key: str, default: Optional[str] = None, **kwargs) -> str:
        """"""

        keys = key.split(".")
        value: Any = self._data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            
            else:
                if default is not None:
                    return default
                
                warning(f"Ключ перевода не найден: {key}")
                return key
            
        
        if value is None:
            if default is not None:
                return default
                
            warning(f"Ключ перевода не найден: {key}")
            return key
        

        if isinstance(value, dict):
            if default is not None:
                return default
            
            warning(f"Ключ перевода указывает на словарь: {key}")
            return key
        
        
        result = str(value)


        if kwargs:
            try:
                result = result.format(**kwargs)

            except KeyError as e:
                warning(f"Отсутствует параметр {e} для ключа {key}")

            except Exception as e:
                warning(f"Ошибка форматирования {key}: {e}")
        
        return result
    

    def set_language(self, lang_code: str) -> None:
        """"""

        if self._lang == lang_code:
            return
        
        self._lang = lang_code
        self._load()
        info(f"Язык изменения на: {lang_code}")

    
    def get_current_language(self) -> str:
        """"""

        return self._lang
    

    def get_available_languages(self) -> List[Tuple[str, str]]:
        """"""

        trans_dir = get_translation_path(DEFAULT_LANGUAGE).parent

        if not trans_dir.exists():
            return [("ru-RU", "Русский")]
        
        language = []

        for file in trans_dir.glob("*.yaml"):
            lang_code = file.stem
            lang_name = self._get_language_name(lang_code)
            language.append((lang_code, lang_name))

        return language
    
    
    def _get_language_name(self, lang_code: str) -> str:
        """"""

        names = {
            "ru-RU": "Русский",
            "en-EN": "English"
        }

        return names.get(lang_code, lang_code)
    

    def reload(self) -> None:
        """"""

        self._load()
        debug(f"Перевод перезагружен: {self._lang}")

    
    def has_key(self, key: str) -> bool:
        """"""

        keys = key.split(".")
        value: Any = self._data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            
            else:
                return False
            

        return value is not None and not isinstance(value, dict)
    

    def get_all_keys(self) -> List[str]:
        """"""

        def _extract_keys(data: Dict, prefix: str = "") -> List[str]:
            keys = []

            for k, v in data.items():
                full_key = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    keys.extend(_extract_keys(v, full_key))

                else:
                    keys.append(full_key)

            return keys
        
        return _extract_keys(self._data)
    

tr = Translator()