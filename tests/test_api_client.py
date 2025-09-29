import unittest
from unittest.mock import patch, Mock
from src.api_client import Parser, HeadHunterAPI


class TestParserBase(unittest.TestCase):

    def test_parser_abstract_methods_present(self):
        # Проверяем, что базовый класс не требует реализации напрямую
        self.assertTrue(hasattr(Parser, "connect"))
        self.assertTrue(callable(getattr(Parser, "connect")))

        self.assertTrue(hasattr(Parser, "get_vacancies"))
        self.assertTrue(callable(getattr(Parser, "get_vacancies")))


class TestHHApiClient(unittest.TestCase):

    def setUp(self):
        self.api = HeadHunterAPI()
        self.api.file_worker = None  # явная настройка
        self.api.__url = "https://api.hh.ru/vacancies"
        self.api.__headers = {"User-Agent": "test-agent"}
        self.api.__params = {}

    def test_connect_sets_status_on_200(self):
        # Подменяем приватный метод __connect через напрямую вызов в тесте (name mangling)
        with patch("src.api_client.requests.get") as mock_get:
            mock_resp = Mock()
            mock_resp.status_code = 200
            mock_get.return_value = mock_resp

            # вызов приватного метода через имя класса (name mangling)
            result = getattr(self.api, "_HeadHunterAPI__connect")()
            self.assertIsNone(result)  # приватный метод ничего не возвращает
            # статус должен быть установлен
            self.assertTrue(getattr(self.api, "_HeadHunterAPI__status"))

    def test_connect_prints_error_on_non_200(self):
        with patch("src.api_client.requests.get") as mock_get, \
                patch("builtins.print") as mock_print:
            mock_resp = Mock()
            mock_resp.status_code = 404
            mock_resp.text = "Not Found"
            mock_get.return_value = mock_resp

            # вызвать приватный метод
            getattr(self.api, "_HeadHunterAPI__connect")()

            mock_print.assert_called_with(
                "Ошибка при запросе: 404 - Not Found"
            )
            self.assertFalse(getattr(self.api, "_HeadHunterAPI__status"))

    def test_get_vacancies_calls_connect_and_fetches_items(self):
        # Подменяем приватный метод __connect и requests.get для fetch вакансий
        with patch("src.api_client.HeadHunterAPI._HeadHunterAPI__connect") as mock_connect, \
             patch("src.api_client.requests.get") as mock_get:

            mock_resp = Mock()
            mock_resp.json.return_value = {"items": [{"url": "http://a", "name": "A"}]}
            mock_get.return_value = mock_resp

            # вызов public метода
            result = self.api.get_vacancies("python")

            # Проверяем, что __connect был вызван
            mock_connect.assert_called_once()

            # Проверяем, что запрос вышел с параметрами text и per_page
            args, kwargs = mock_get.call_args
            # URL в первый аргумент, параметры в kwargs['params']
            self.assertIn('text', kwargs['params'])
            self.assertIn('per_page', kwargs['params'])

            # Проверяем возвращаемые данные
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['name'], "A")


if __name__ == '__main__':
    unittest.main()
