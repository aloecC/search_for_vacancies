from abc import ABC, abstractmethod


class BaseApiClient(ABC):
    @abstractmethod
    def connecting_to_the_api(self):
        """Метод подключения к API."""
        pass

    @abstractmethod
    def receiving_vacancies_separately(self):
        """Метод получения вакансий отдельно"""
        pass


class HHApiClient(BaseApiClient):
    def connecting_to_the_api(self):
        """Метод подключения к API."""
        pass
    # реализовать вызов в __receiving_vacancies_separately перед отправкой запроса
    # реализовать отправку запроса на базовый URL
    # реализовать проверку статус-кода ответа

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