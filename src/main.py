import sys
from PySide6.QtWidgets import QApplication

from src.controllers.auth_controller import AuthController
from src.views.login_window import LoginWindow
from src.views.create_vault import CreateWindow
from src.views.main_window import MainWindow
from src.utils.logger import info, error


def main():
    app = QApplication(sys.argv)

    auth = AuthController()
    if auth.is_first_run():
        info("Первый запуск - создание хранилища")
        create_window = CreateWindow(auth)

        if not create_window.exec():
            info("Создание хранилища отменено, выход")
            return

        info("Хранилище создано, переходим ко входу")

    info("Вход в хранилище")
    login_window = LoginWindow(auth)

    if not login_window.exec():
        info("Вход отменён, выход")
        return

    controller = auth.get_password_controller()
    if controller is None:
        error("Не удалось получить контроллер")
        return

    main_window = MainWindow(controller)

    main_window.lock_vault.connect(lambda: on_lock(auth, main_window))

    main_window.show()

    sys.exit(app.exec())


def on_lock(auth: AuthController, main_window: MainWindow):
    info("Блокировка хранилища")

    main_window.close()

    auth.lock_vault()

    login_window = LoginWindow(auth)

    if login_window.exec():
        controller = auth.get_password_controller()
        if controller:
            new_window = MainWindow(controller)
            new_window.lock_vault.connect(lambda: on_lock(auth, new_window))
            new_window.show()
    else:
        info("Вход отменён, выход")
        QApplication.quit()
