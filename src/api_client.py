from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    @abstractmethod
    def connecting_to_the_api(self):
        """Метод подключения к API."""
        pass

    @abstractmethod
    def receiving_vacancies_separately(self):
        """Метод получения вакансий отдельно"""
        pass


class HH(Parser):

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def connecting_to_the_api(self):
        """Метод подключения к API."""
        pass
    # реализовать вызов в __receiving_vacancies_separately перед отправкой запроса
    # реализовать отправку запроса на базовый URL
    # реализовать проверку статус-кода ответа
    # Ссылка на API: https://github.com/hhru/api/.

    def __receiving_vacancies_separately(self):
        """Приватный метод получения вакансий отдельно"""
        pass

    def receiving_data(self, keyword):
        """Метод получения данных"""
        pass
    # реализовать формирование параметров для запроса из text и per_page
    # реализовать отправку запроса на API hh.ru для получения данных о вакансиях по keyword
    # реализовать сбор данных ответа в формате списка словарей из ключа item
    # per_page — количество элементов, отображаемых на одной странице результатов при получении данных с веб-сервиса или сайта.
    # text - строковая переменная в Python, которая хранит HTML-код, полученный с веб-страницы.