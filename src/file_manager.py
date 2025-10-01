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
    def __init__(self, js_file=None):
        super().__init__()
        if js_file is None:
            self.__js_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'user_vacancies.json')
        else:
            self.__js_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), f'{js_file}')

    def receiving_data_from_a_file(self):
        """Метод получения данных из файла"""
        if not os.path.exists(self.__js_file):
            # Если файла нет, вернуть пустой список
            return []
        with open(self.__js_file, 'r', encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            return data

    def check_data_to_file(self, item):
        """Метод проверки наличия словаря в файле"""
        current_data = self.receiving_data_from_a_file()
        if item in current_data:
            return False
        else:
            return True

    def adding_data_to_file(self, new_data):
        """Метод добавления данных в файл"""
        # Получаем текущие данные (если файла нет или он пустой — пустой список)
        current_data = self.receiving_data_from_a_file()

        # Приводим новый объект Vacancy к словарю
        if isinstance(new_data, Vacancy):
            item = new_data.to_dict()
            if self.check_data_to_file(item) is False:
                return
            current_data.append(item)
            # Сохраняем обратно в файл
            with open(self.__js_file, 'w', encoding="utf-8") as file:
                json.dump(current_data, file, ensure_ascii=False, indent=4)
        elif isinstance(new_data, dict):
            item = new_data
            if self.check_data_to_file(item) is False:
                return
            current_data.append(item)
            # Сохраняем обратно в файл
            with open(self.__js_file, 'w', encoding="utf-8") as file:
                json.dump(current_data, file, ensure_ascii=False, indent=4)
        elif isinstance(new_data, list):
            for f in new_data:
                item = f.to_dict()
                if self.check_data_to_file(item) is False:
                    return
                current_data.append(item)
                # Сохраняем обратно в файл
                with open(self.__js_file, 'w', encoding="utf-8") as file:
                    json.dump(current_data, file, ensure_ascii=False, indent=4)
        else:
            # Неизвестный тип - ничего не добавляем
            return

    def deleting_data_from_a_file(self, del_data):
        """Метод удаления данных из файла"""
        current_data = self.receiving_data_from_a_file()
        if isinstance(del_data, Vacancy):
            target = del_data.to_dict()
        elif isinstance(del_data, dict):
            target = del_data
        else:
            return
        if isinstance(current_data, list):
            # Поиск индекса элемента, совпадающего по значениям словаря
            index_to_remove = None
            for idx, item in enumerate(current_data):
                if isinstance(item, dict) and item == target:
                    index_to_remove = idx
                    break
            if index_to_remove is not None:
                current_data.pop(index_to_remove)
                with open(self.__js_file, 'w', encoding='utf-8') as file:
                    json.dump(current_data, file, ensure_ascii=False, indent=4)










