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
        if not os.path.exists(self._js_file):
            # Если файла нет, вернуть пустой список
            return []
        with open(self._js_file, 'r', encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            return data

    def adding_data_to_file(self, new_data):
        """Метод добавления данных в файл"""
        # Получаем текущие данные (если файла нет или он пустой — пустой список)
        current_data = self.receiving_data_from_a_file()

        # Приводим новый объект Vacancy к словарю
        if isinstance(new_data, Vacancy):
            new_item = vars(new_data)
        elif isinstance(new_data, dict):
            new_item = new_data
        else:
            # Неизвестный тип - ничего не добавляем
            return
        current_data.append(new_item)
        # Сохраняем обратно в файл
        with open(self._js_file, 'w', encoding="utf-8") as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)



    #Файл не перезаписывается
    #Файл не сохраняет дубли вакансий
    #Файл является списком словарей

    def deleting_data_from_a_file(self, del_data):
        """Метод удаления данных из файла"""
        pass









