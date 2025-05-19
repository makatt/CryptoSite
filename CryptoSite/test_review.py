import unittest
from routes import validate_phone, validate_date

class Test_test_review(unittest.TestCase):
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
        self.assertFalse(validate_date('2024-5-9'))     # мес€ц и день не 2 знака
        self.assertFalse(validate_date('20240519'))     # нет разделителей
        self.assertFalse(validate_date('abcd-ef-gh'))   # буквы

if __name__ == '__main__':
    unittest.main()
