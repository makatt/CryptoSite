import unittest
from datetime import datetime
import re
from routes import add_crypto  # Импортируем функцию добавления криптовалюты

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
