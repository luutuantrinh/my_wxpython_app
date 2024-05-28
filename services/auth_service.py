from utils.encryption import encrypt_data, decrypt_data, generate_key
from utils.file_manager import load_users, save_users
from config.settings import SECRET_KEY

class AuthService:
    def __init__(self):
        self.users = load_users()

    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        user_key = generate_key()
        encrypted_password = encrypt_data(password, user_key)
        self.users[username] = {
            'password': encrypted_password.decode(),
            'secret_key': user_key.decode()
        }
        save_users(self.users)

    def validate_user(self, username, password):
        if username in self.users:
            encrypted_password = self.users[username]['password']
            user_key = self.users[username]['secret_key']
            decrypted_password = decrypt_data(encrypted_password, user_key)
            return decrypted_password == password
        return False

    def validate_secret_key(self, username, secret_key):
        if username in self.users:
            user_key = self.users[username]['secret_key']
            return user_key == secret_key
        return False

    def get_secret_key(self, username):
        if username in self.users:
            return self.users[username]['secret_key']
        return None
