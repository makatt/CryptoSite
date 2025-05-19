import unittest
from routes import validate_phone, validate_date

class Test_test_review(unittest.TestCase):
     def test_validate_phone_valid(self):
        self.assertTrue(validate_phone('+71234567890'))

     def test_validate_phone_invalid(self):
        self.assertFalse(validate_phone('81234567890'))     # ��� +
        self.assertFalse(validate_phone('+7123456789'))     # 9 ���� ����� +7
        self.assertFalse(validate_phone('+712345678901'))   # 11 ���� ����� +7
        self.assertFalse(validate_phone('+7abcdefghij'))    # �����

     def test_validate_date_valid(self):
        self.assertTrue(validate_date('2024-05-19'))
        self.assertTrue(validate_date('1999-12-31'))

     def test_validate_date_invalid(self):
        self.assertFalse(validate_date('24-05-19'))     # �������� ������
        self.assertFalse(validate_date('2024/05/19'))   # �������� �����������
        self.assertFalse(validate_date('2024-5-9'))     # ����� � ���� �� 2 �����
        self.assertFalse(validate_date('20240519'))     # ��� ������������
        self.assertFalse(validate_date('abcd-ef-gh'))   # �����

if __name__ == '__main__':
    unittest.main()
