from src.api_client import HeadHunterAPI

class BaseVacancyService:
    #Реализовать __slots__ для экономии данных
    pass

    def __init__(self, name, url, salary, requirement):
        self.url = url
        self.job_title = name
        self.salary = salary
        self.requirement = requirement
        self.lst_vacancy = []

    def compare_hour_ly_wage(self):
        """метод сравнения вакансий с повременной оплатой."""
        pass

    def compare_piece_rate(self):
        """метод сравнения вакансий с сдельной оплатой."""
        pass

    def compare_wage_types(self):
        """метод сравнения вакансий с разными типами оплаты."""
        pass

    def __data_validation_time_based_payment(self):
        """метод валидации данных (повременный расчет)"""
        #Используется при инициализации атрибутов
        pass

    def __data_validation_urgent_payment(self):
        """метод валидации данных (сдельный расчет)"""
        # Используется при инициализации атрибутов
        pass

