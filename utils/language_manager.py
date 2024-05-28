import json
import os

class LanguageManager:
    def __init__(self, language='en'):
        self.language = language
        self.language_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'languages.json')
        self.load_language()

    def load_language(self):
        with open(self.language_file, 'r', encoding='utf-8') as file:
            self.languages = json.load(file)

    def set_language(self, language):
        self.language = language

    def get(self, key):
        return self.languages.get(self.language, {}).get(key, key)

# Khởi tạo một đối tượng LanguageManager toàn cục với ngôn ngữ mặc định là tiếng Anh
language_manager = LanguageManager('en')
