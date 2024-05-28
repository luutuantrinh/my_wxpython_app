from services.auth_service import AuthService
from views.login_view import LoginView
from views.main_view import MainView
from views.secret_login_view import SecretLoginView
from views.splash_screen import SplashScreen
from views.main_app_view import MainAppView
from utils.language_manager import language_manager

class LoginController:
    def __init__(self):
        self.auth_service = AuthService()
        self.main_view = MainView(None, title="Main", controller=self)
        self.login_view = None
        self.secret_login_view = None
        self.splash_screen = None

    def show_view(self):
        self.main_view.Show()

    def show_login_view(self):
        self.login_view = LoginView(None, title="Login", controller=self)
        self.login_view.Show()

    def show_register_view(self):
        from controllers.register_controller import RegisterController
        self.register_controller = RegisterController()
        self.register_controller.show_view()

    def show_secret_login_view(self):
        self.secret_login_view = SecretLoginView(None, title="Login with Secret Key", controller=self)
        self.secret_login_view.Show()

    def handle_login(self, username, password):
        if self.auth_service.validate_user(username, password):
            self.show_splash_screen()
        else:
            self.login_view.show_message(language_manager.get('login_failed'))

    def handle_secret_login(self, username, secret_key):
        if self.auth_service.validate_secret_key(username, secret_key):
            self.show_splash_screen()
        else:
            self.secret_login_view.show_message(language_manager.get('login_failed'))

    def show_splash_screen(self):
        self.splash_screen = SplashScreen(
            image_path="media/pngwing.com.png",
            duration=3000,
            callback=self.show_main_app_view
        )
        self.splash_screen.Show()

    def show_main_app_view(self):
        if self.main_view:
            self.main_view.Destroy()
        if self.login_view:
            self.login_view.Destroy()
        if self.secret_login_view:
            self.secret_login_view.Destroy()
        if self.splash_screen:
            self.splash_screen.Destroy()
        self.main_app_view = MainAppView(None, title="Main Application")
        self.main_app_view.Show()
