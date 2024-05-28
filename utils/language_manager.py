import json
import os

class LanguageManager:
    def __init__(self, default_lang='en'):
        self.lang = default_lang
        self.load_language_content()

    def load_language_content(self):
        lang_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'languages.json')
        with open(lang_file_path, 'r', encoding='utf-8') as f:
            self.languages = json.load(f)

    def set_language(self, lang):
        if lang in self.languages:
            self.lang = lang

    def get(self, key):
        return self.languages.get(self.lang, {}).get(key, key)

language_manager = LanguageManager()
