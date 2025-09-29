from __future__ import annotations
from abc import ABC, abstractmethod
import requests
from typing import List, Dict


class Parser(ABC):
    """
    Абстрактный базовый класс для работы с API сервисов вакансий.
    """
    def __init__(self):
        pass
    @abstractmethod
    def connect(self) -> None:
        """Установить соединение с API (проверка доступности)."""
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получить вакансии по ключевому слову. Возвращает список словарей."""
        raise NotImplementedError


class HeadHunterAPI(Parser):
    """
    Реализация Parser для hh.ru (HeadHunter).
    """

    def __init__(self, file_worker):
        # приватные атрибуты экземпляра
        self.__url = 'https://github.com/hhru/api/'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        self.__file_worker = file_worker
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

    def __connecting(self):
        """Приватный метод подключения к API."""
        pass

    # реализовать вызов в receiving_data перед отправкой запроса
    # реализовать отправку запроса на базовый URL
    # реализовать проверку статус-кода ответа
    # Ссылка на API: https://github.com/hhru/api/.

    def connecting(self):
        """Публичный метод подключения к API."""
        self.__connecting()

    def get_vacancies_separately(self):
        """Метод получения вакансий отдельно"""
        pass

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получить вакансии по ключевому слову. Возвращает список словарей."""
        pass


