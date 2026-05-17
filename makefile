# Makefile для KeyKeeper
# Команды:

.PHONY: run install venv help init

# Переменные
PYTHON = python3
VENV = venv

VENV_BIN = $(VENV)/bin
REQ = requirements.txt


# Цвета
GREEN = \033[0;32m
RED = \033[0;31m
YELLOW = \033[0;33m
NC = \033[0m


#
#
#

run: ## Запуск приложения
	@echo "$(GREEN) Запуск KeyKeeper...$(NC)"
	$(PYTHON) run.py


#
#
#

install: ## Установка зависимостей
	@echo "$(GREEN) Установка зависимостей...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(REQ)
	@echo "$(GREEN) Готово!$(NC)"


venv: ## Создание виртуального окружения
	@echo "$(GREEN) Создание виртуального окружения...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN) Готово!$(NC)"


init: ## Полный запуск проекта
	make venv
	. $(VENV_BIN)/activate && make install
	. $(VENV_BIN)/activate && $(PYTHON) run.py


fresh: ## Полная очистка проекта
	@echo "$(GREEN) Удаление виртуального окружения...$(NC)"
	rm -rf $(VENV)
	@echo "$(GREEN) Успешно$(NC)"
	@echo
	@echo "$(GREEN) Удаление pycache ....$(NC)"
	find . -type d -name 	"__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN) Успешно$(NC)"

	make venv
	. $(VENV_BIN)/activate && make install

clear: ## Очистка временных файлов
	@echo "$(GREEN) Удаление pycache ....$(NC)"
	find . -type d -name 	"__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN) Успешно$(NC)"

#
#
#

help: ## Справка
	@echo "$(YELLOW)KeyKeeper - доступные команды:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""
