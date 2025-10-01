import json
import os
import sys
import unittest
from unittest.mock import mock_open, patch
from src.file_manager import JSONSaver
from src.vacancy_service import Vacancy


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000-150000", "Требования: опыт работы от 3 лет...")
        self.js_file = JSONSaver('test_user_vacancies.json')

    @patch('os.path.exists')
    def test_file_does_not_exist(self, mock_exists):
        mock_exists.return_value = False
        self.assertEqual(self.js_file.receiving_data_from_a_file(), [])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_file_exists_with_valid_json(self, mock_open, mock_exists):
        mock_exists.return_value = True  # Файл существует
        self.assertEqual(self.js_file.receiving_data_from_a_file(), {"key": "value"})  # Проверка на корректные данные

    def test_adding_new_dict_when_file_is_empty(self):
        vacancy2 = Vacancy("Developer", "<https://hh.ru/vacancy/123456>", "200000-250000", "Требования: опыт работы от 3 лет...")
        self.js_file.adding_data_to_file(vacancy2)
        item = vacancy2.to_dict()
        self.assertEqual(self.js_file.check_data_to_file(item), False)

    def test_deleting_data_from_a_file(self):
        vacancy2 = Vacancy("Developer", "<https://hh.ru/vacancy/123456>", "200000-250000",
                           "Требования: опыт работы от 3 лет...")
        self.js_file.deleting_data_from_a_file(vacancy2)
        item = vacancy2.to_dict()
        self.assertEqual(self.js_file.check_data_to_file(item), True)



if __name__ == '__main__':
    unittest.main()
