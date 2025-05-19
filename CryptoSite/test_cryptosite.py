import unittest
import re
from datetime import datetime
from routes import validate_phone, validate_date
import re
from routes import add_crypto
from routes import add_btc_review

def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_phone(phone_text):
    return re.match(r'^\+?\d[\d\s\-]{7,}$', phone_text) is not None

class DummySaveJson:
    def __init__(self):
        self.called = False
        self.last_data = None

    def __call__(self, filepath, data):
        self.called = True
        self.last_data = data

class TestArticleValidation(unittest.TestCase):
    # --- Даты ---
    def test_valid_date_format(self):
        self.assertTrue(is_valid_date("2023-12-31"))

    def test_invalid_date_format_day(self):
        self.assertFalse(is_valid_date("2023-02-30")) 

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
    def test_date_edge_leap_year(self):
        self.assertTrue(is_valid_date("2024-02-29"))  # Високосный год

    def test_phone_with_multiple_spaces(self):
        self.assertTrue(is_valid_phone("+7  999  555  3333"))  # Лишние пробелы допустимы

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

class TestAddReview(unittest.TestCase):
     def test_validate_phone_valid(self):
        self.assertTrue(validate_phone('+71234567890'))

     def test_validate_phone_invalid(self):
        self.assertFalse(validate_phone('81234567890'))     # без +
        self.assertFalse(validate_phone('+7123456789'))     # 9 цифр после +7
        self.assertFalse(validate_phone('+712345678901'))   # 11 цифр после +7
        self.assertFalse(validate_phone('+7abcdefghij'))    # буквы

     def test_validate_date_valid(self):
        self.assertTrue(validate_date('2024-05-19'))
        self.assertTrue(validate_date('1999-12-31'))

     def test_validate_date_invalid(self):
        self.assertFalse(validate_date('24-05-19'))     # неверный формат
        self.assertFalse(validate_date('2024/05/19'))   # неверный разделитель
        self.assertFalse(validate_date('2024-5-9'))     # месяц и день не 2 знака
        self.assertFalse(validate_date('20240519'))     # нет разделителей
        self.assertFalse(validate_date('abcd-ef-gh'))   # буквы

     def setUp(self):
        # "Заглушка" для save_json
        self.dummy_save = DummySaveJson()
        import routes
        self.old_save_json = routes.save_json
        routes.save_json = self.dummy_save

     def tearDown(self):
        # Восстановить оригинал после тестов
        import routes
        routes.save_json = self.old_save_json

     def test_add_btc_review_all_valid(self):
        form_data = {'name': 'Иван', 'text': 'Все отлично', 'phone': '+71234567890'}
        btc_reviews = []
        reviews_all = {}
        error, cleaned = add_btc_review(form_data, btc_reviews, reviews_all)
        self.assertIsNone(error)
        self.assertEqual(cleaned, {})
        self.assertEqual(len(btc_reviews), 1)
        self.assertEqual(btc_reviews[0]['name'], 'Иван')
        self.assertEqual(btc_reviews[0]['phone'], '+71234567890')
        self.assertIn('date', btc_reviews[0])
        self.assertTrue(self.dummy_save.called)
        self.assertIn('bitcoin', self.dummy_save.last_data)
        self.assertIsInstance(self.dummy_save.last_data['bitcoin'], list)

     def test_add_btc_review_empty_fields(self):
        # Пустое имя
        form_data = {'name': '', 'text': 'Все отлично', 'phone': '+71234567890'}
        btc_reviews = []
        reviews_all = {}
        error, cleaned = add_btc_review(form_data, btc_reviews, reviews_all)
        self.assertEqual(error, 'Пожалуйста, заполните все поля.')
        self.assertEqual(cleaned, form_data)
        self.assertEqual(btc_reviews, [])

        # Пустой текст
        form_data = {'name': 'Иван', 'text': '', 'phone': '+71234567890'}
        error, cleaned = add_btc_review(form_data, btc_reviews, reviews_all)
        self.assertEqual(error, 'Пожалуйста, заполните все поля.')

        # Пустой телефон
        form_data = {'name': 'Иван', 'text': 'Все отлично', 'phone': ''}
        error, cleaned = add_btc_review(form_data, btc_reviews, reviews_all)
        self.assertEqual(error, 'Пожалуйста, заполните все поля.')

     def test_add_btc_review_invalid_phone(self):
        form_data = {'name': 'Иван', 'text': 'Все отлично', 'phone': '123456'}
        btc_reviews = []
        reviews_all = {}
        error, cleaned = add_btc_review(form_data, btc_reviews, reviews_all)
        self.assertEqual(error, 'Телефон должен быть в формате +7XXXXXXXXXX')
        self.assertEqual(cleaned, form_data)
        self.assertEqual(btc_reviews, [])
 
     def test_add_btc_review_multiple(self):
        # Первый отзыв
        form_data1 = {'name': 'Иван', 'text': 'Отлично', 'phone': '+71234567890'}
        btc_reviews = []
        reviews_all = {}
        add_btc_review(form_data1, btc_reviews, reviews_all)
        # Второй отзыв
        form_data2 = {'name': 'Анна', 'text': 'Хорошо', 'phone': '+79876543210'}
        add_btc_review(form_data2, btc_reviews, reviews_all)
        self.assertEqual(btc_reviews[0]['name'], 'Анна')
        self.assertEqual(btc_reviews[1]['name'], 'Иван')
        self.assertEqual(len(btc_reviews), 2)
        self.assertEqual(reviews_all['bitcoin'][0]['name'], 'Анна')
        self.assertEqual(reviews_all['bitcoin'][1]['name'], 'Иван')


class TestCryptoInputValidation(unittest.TestCase):
    def test_valid_date_format(self):
        """Проверка корректной даты в формате YYYY-MM-DD"""
        date_str = "2023-01-15"
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            actual = True
        except ValueError:
            actual = False
        self.assertTrue(actual, "Корректная дата не прошла валидацию")

    def test_valid_url_with_https(self):
        """Проверка корректного HTTPS URL"""
        url = "https://example.com "
        url = url.strip()
        pattern = re.compile(
            r'^https?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        actual = bool(pattern.match(url))
        self.assertTrue(actual, "Корректный HTTPS URL не прошёл валидацию")

    def test_valid_url_with_http(self):
        """Проверка корректного HTTP URL"""
        url = "http://example.com"
        url = url.strip()
        pattern = re.compile(
            r'^https?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        actual = bool(pattern.match(url))
        self.assertTrue(actual, "Корректный HTTP URL не прошёл валидацию")

    def test_valid_url_with_path_and_port(self):
        """Проверка корректного URL с путём и портом"""
        url = "https://example.com:8080/path/to/page "
        url = url.strip()
        pattern = re.compile(
            r'^https?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        actual = bool(pattern.match(url))
        self.assertTrue(actual, "URL с путём и портом не прошёл валидацию")

    def test_valid_url_with_query_params(self):
        """Проверка корректного URL с параметрами"""
        url = "https://example.com?utm_source=google "
        url = url.strip()
        pattern = re.compile(
            r'^https?://'  
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  
            r'localhost|'  
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
            r'(?::\d+)?'  
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        actual = bool(pattern.match(url))
        self.assertTrue(actual, "URL с параметрами не прошёл валидацию")


class TestAddCryptoFunction(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.valid_data = {
            'title': 'Bitcoin',
            'symbol': 'BTC',
            'date': '2023-01-01',
            'price': '45000.50',
            'website': 'https://bitcoin.org ',
            'content': 'Первая и самая известная криптовалюта',
            'status': 'active'
        }

if __name__ == '__main__':
    unittest.main()
