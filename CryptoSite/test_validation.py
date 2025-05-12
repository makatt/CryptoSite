import unittest
import re
from datetime import datetime

# Допустим, у тебя есть валидаторы где-то в routes.py или отдельном модуле
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_phone(phone_text):
    return re.match(r'^\+?\d[\d\s\-]{7,}$', phone_text) is not None

class TestArticleValidation(unittest.TestCase):

    # --- Даты ---
    def test_valid_date_format(self):
        self.assertTrue(is_valid_date("2023-12-31"))

    def test_invalid_date_format_day(self):
        self.assertFalse(is_valid_date("2023-02-30"))  # не существует

    def test_invalid_date_format_wrong_sep(self):
        self.assertFalse(is_valid_date("2023/12/31"))

    def test_invalid_date_non_date(self):
        self.assertFalse(is_valid_date("тридцать первое декабря"))

    # --- Телефоны ---
    def test_valid_phone_international(self):
        self.assertTrue(is_valid_phone("+7 123 456 7890"))

    def test_valid_phone_with_dashes(self):
        self.assertTrue(is_valid_phone("8-800-555-35-35"))

    def test_invalid_phone_letters(self):
        self.assertFalse(is_valid_phone("ABCD1234"))

    def test_invalid_phone_too_short(self):
        self.assertFalse(is_valid_phone("12345"))

    def test_invalid_phone_special_chars(self):
        self.assertFalse(is_valid_phone("+7 (123) 456*7890"))

    # --- Интеграция всех полей (пример) ---
    def test_form_all_fields_correct(self):
        name = "Иван"
        text = "Полезная статья"
        date = "2024-05-11"
        phone = "+7 999 888 7766"
        self.assertTrue(name)
        self.assertTrue(text)
        self.assertTrue(is_valid_date(date) or is_valid_phone(phone))

    def test_form_missing_fields(self):
        name = ""
        text = ""
        date = "invalid-date"
        phone = ""
        self.assertFalse(name)
        self.assertFalse(text)
        self.assertFalse(is_valid_date(date))
        self.assertFalse(is_valid_phone(phone))

if __name__ == '__main__':
    unittest.main()
