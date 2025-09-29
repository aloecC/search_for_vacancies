from abc import ABC, abstractmethod
import json
#Реализовать доп классы для работы с файлами


class BaseFileManager(ABC):

    @abstractmethod
    def display_last_transactions(self):
        """Метод чтения json-файла"""
        pass

    @abstractmethod
    def receiving_data_from_a_file(self):
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def adding_data_to_file(self):
        """Метод добавления данных в файл"""
        pass

    @abstractmethod
    def deleting_data_from_a_file(self):
        """Метод удаления данных из файла"""
        pass


class JsonDataStorage(BaseFileManager):

    def __init__(self, js_file=None):
        if js_file is None:
            self._js_file = []
        else:
            self._js_file = js_file

    def receiving_data_from_a_file(self):
        """Метод получения данных из файла"""
        pass

    def adding_data_to_file(self):
        """Метод добавления данных в файл"""
        pass
    #Файл не перезаписывается
    #Файл не сохраняет дубли вакансий
    #Файл является списком словарей

    def deleting_data_from_a_file(self):
        """Метод удаления данных из файла"""
        pass









