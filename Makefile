
run:  ## Запустить проект
	.venv/bin/python run.py

run_test: ## Запустить тест
	.venv/bin/python run_test.py

venv: ## Создать .venv и установить зависимости
	python3 -m venv .venv && \
	.venv/bin/pip install --upgrade pip && \
	.venv/bin/pip install -r requirements.txt
	source .venv/bin/activate

delete_venv:
	rm -rf .venv

init: venv run ## Установить всё необходимое и запустить проект


help: ## Показать справку
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS=":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
