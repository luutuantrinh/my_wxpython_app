from services.auth_service import AuthService
from views.register_view import RegisterView
from utils.logger import app_logger

class RegisterController:
    def __init__(self):
        self.auth_service = AuthService()
        self.view = RegisterView(None, title="Register", controller=self)

    def show_view(self):
        self.view.Show()

    def handle_register(self, username, password):
        if self.auth_service.user_exists(username):
            app_logger.warning(f"Failed to create account: User {username} already exists")
        else:
            try:
                self.auth_service.register_user(username, password)
                self.view.show_message("Registration successful!")
            except ValueError as e:
                self.view.show_message(str(e))
