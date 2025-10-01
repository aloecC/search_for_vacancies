import os
import sys
from abc import ABC, abstractmethod
import json

from src.vacancy_service import Vacancy


#Реализовать доп классы для работы с файлами


class BaseFileManager(ABC):

    @abstractmethod
    def receiving_data_from_a_file(self):
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def adding_data_to_file(self, new_data):
        """Метод добавления данных в файл"""
        pass

    @abstractmethod
    def deleting_data_from_a_file(self, del_data):
        """Метод удаления данных из файла"""
        pass


class JSONSaver(BaseFileManager):
    def __init__(self):
        super().__init__()
        self._js_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'user_vacancies.json')

    def receiving_data_from_a_file(self):
        """Метод получения данных из файла"""
        with open(self._js_file, 'r', encoding="utf-8") as file:
            file = json.load(file)
            return file

    def adding_data_to_file(self, new_data):
        """Метод добавления данных в файл"""
        if os.path.exists('user_vacancies.json'):
            current_data = self.receiving_data_from_a_file()
            if isinstance(new_data, Vacancy):
                current_data.append(vars(new_data))



    #Файл не перезаписывается
    #Файл не сохраняет дубли вакансий
    #Файл является списком словарей

    def deleting_data_from_a_file(self, del_data):
        """Метод удаления данных из файла"""
        pass









