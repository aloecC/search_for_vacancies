from __future__ import annotations
from abc import ABC, abstractmethod
import requests
from typing import List, Dict


class Parser(ABC):
    """
    Абстрактный базовый класс для работы с API сервисов вакансий.
    """
    def __init__(self, file_worker=None):
        self.file_worker = file_worker

    @abstractmethod
    def connect(self) -> None:
        """Установить соединение с API (проверка доступности)."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получить вакансии по ключевому слову. Возвращает список словарей."""
        pass


class HeadHunterAPI(Parser):
    """
    Реализация Parser для hh.ru (HeadHunter).
    """

    def __init__(self, file_worker=None):
        # приватные атрибуты экземпляра
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        self.__vacancies_keyword = []
        self.__status = False
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

    def __connect(self):
        """Приватный метод подключения к API."""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            self.__status = True
        else:
            print(f"Ошибка при запросе: {response.status_code} - {response.text}")

    def connect(self):
        """Публичный метод подключения к API."""
        return self.__connect()

    def get_vacancies(self, keyword: str, per_page=25) -> List[Dict]:
        """Получить вакансии по ключевому слову. Возвращает список словарей."""
        self.__vacancies_keyword = []
        self.__params['text'] = keyword
        self.__params['per_page'] = per_page
        self.__connect()
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        self.__vacancies_keyword = response.json().get('items', [])
        return self.__vacancies_keyword

    def get_vacancies_separately(self):
        """Метод получения вакансий отдельно"""
        return self.__vacancies
